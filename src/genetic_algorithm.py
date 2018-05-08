# Imports
import random
import copy
import numpy as np
import math
import sys

#import genetic_stats

from project_setup import Project
from defaults import AMOUNT_OF_WORKERS


class GeneticAlgorithm:
    def __init__(self, components):
        self.components = components

        self.best_project = None
        self.best_fitness = -1

        self._generate_population(components)

    """ Generate initial population """
    def _generate_population(self, components, size=100):
        self.population = []
        for i in range(0, size):
            for comp in components:
                comp.change_workers(self._get_random_workers())
            self.population.append(Project(components))

    """ Generate an array of the fitness's given the population """
    def _generate_fitnesses(self):
        self.fitnesses = []
        for project in self.population:
            self.fitnesses.append(project.calc_fitness())

    """ Get a random amount of workers based on a normal distribution with mean #WORKERS/2 """
    def _get_random_workers(self):
        return int(np.random.normal(AMOUNT_OF_WORKERS / 2, math.sqrt(AMOUNT_OF_WORKERS / 2)))

    """ Get a random amount of workers given the current amount of workers base on a normal distribtuion with mean
    the given current amount of workers"""
    def _get_new_random_workers(self, workers):
        return int(np.random.normal(workers, math.sqrt(20)))

    """ Get a random index based on a triangular distribution starting from 0 coming down to #WORKERS/2 """
    def _get_random_project_to_breed(self):
        return int(np.random.triangular(0, 0, AMOUNT_OF_WORKERS / 2))

    """ Create #amount of new projects by crossbreeding the best ones """
    def _crossbreed(self, amount=30):
        self._generate_fitnesses()
        indexes = np.array(self.fitnesses).argsort()

        for i in range(0, amount):
            self.population[indexes[len(indexes) - i - 1]] = \
                self._crossbreed_projects(indexes[self._get_random_project_to_breed()],
                                          indexes[self._get_random_project_to_breed()])

    """ Create a new child (crossbred project) given the 2 indexes of the parents """
    def _crossbreed_projects(self, i1, i2):
        new_components = copy.deepcopy(self.population[i1].components)
        for i in range(random.randint(1, AMOUNT_OF_WORKERS - 1), len(self.population[0].components)):
            new_components[i] = self.population[i2].components[i]
        return Project(new_components)

    """ Mutate the population """
    def _mutate(self, prob=0.3):
        for i in range(0, len(self.population)):
            if random.random() < prob:
                comps = self.population[i].components
                for j in range(0, len(comps)):
                    if random.random() < prob:
                        comps[j].change_workers(self._get_new_random_workers(comps[j].assigned_workers))
                self.population[i] = Project(comps)

    """ Run the genetic algorithm for #iterations generations """
    def run(self, iterations):
        print("Running genetic algorithm for", iterations, "iterations...")
        for i in range(0, iterations):
            self._crossbreed()
            self._mutate()

            self._generate_fitnesses()

            print(i, '\tBest fitness', min(self.fitnesses))

            if (min(self.fitnesses) < self.best_fitness) or (self.best_fitness == -1):
                self.best_fitness = min(self.fitnesses)
                self.best_project = copy.deepcopy(self.population[np.argmin(self.fitnesses)])

                print("Duration of project with best fitness: ", self.best_project.get_duration())
            genetic_stats.log_stats(self.best_project)
        #genetic_stats.plot_stats()
        print("End fitness", self.best_fitness)

    def get_best_project(self):
        return self.best_project
