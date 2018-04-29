# Imports
import random
import copy
import numpy as np
import math

import stats

from project_setup import Project, AMOUNT_OF_WORKERS


class GeneticAlgorithm:
    def __init__(self, components):
        self.components = components

        self.best_project = Project(self.components)
        self.best_fitness = self.best_project.calc_fitness()

        # self.min_fitness = self.best_project.calc_max_fitness()
        # self.max_fitness = self.best_project.calc_min_fitness()

        self._generate_population(components)

    def _generate_population(self, components, size=100):
        self.population = []
        for i in range(0, size):
            for comp in components:
                comp.change_workers(self._get_random_workers())
            self.population.append(Project(components))

    def _generate_fitnesses(self):
        self.fitnesses = []
        for project in self.population:
            self.fitnesses.append(project.calc_fitness())

    def _get_random_workers(self):
        return int(np.random.normal(AMOUNT_OF_WORKERS / 2, math.sqrt(AMOUNT_OF_WORKERS / 2)))

    def _get_new_random_workers(self, workers):
        return int(np.random.normal(workers, math.sqrt(20)))

    def _get_random_project_to_breed(self):
        return int(np.random.triangular(0, 0, AMOUNT_OF_WORKERS / 2))

    def _crossbreed(self, amount=30):
        self._generate_fitnesses()
        indexes = np.array(self.fitnesses).argsort()

        for i in range(0, amount):
            self.population[indexes[len(indexes) - i - 1]] = \
                self._crossbreed_projects(indexes[self._get_random_project_to_breed()],
                                          indexes[self._get_random_project_to_breed()])

    def _crossbreed_projects(self, i1, i2):
        new_components = copy.deepcopy(self.population[i1].components)
        for i in range(random.randint(1, AMOUNT_OF_WORKERS - 1), len(self.population[0].components)):
            new_components[i] = self.population[i2].components[i]
        return Project(new_components)

    def _mutate(self):
        for i in range(0, len(self.population)):
            if random.random() < 0.3:
                comps = self.population[i].components
                for j in range(0, len(comps)):
                    if random.random() < 0.3:
                        comps[j].change_workers(self._get_new_random_workers(comps[j].assigned_workers))
                self.population[i] = Project(comps)

    def run(self, iterations):
        print("Running genetic algorithm for", iterations, "iterations...")
        for i in range(0, iterations):
            self._crossbreed()
            self._mutate()

            self._generate_fitnesses()

            print(i, '\tBest fitness', min(self.fitnesses))

            if min(self.fitnesses) < self.best_fitness:
                self.best_fitness = min(self.fitnesses)
                self.best_project = copy.deepcopy(self.population[np.argmin(self.fitnesses)])

                # TODO De lijn hieronder was "stats.log_stats(current_project)" @Nick, kheb da aangepast, ist just?
                # stats.log_stats(self.best_project)
        # stats.plot_stats()
        print("End fitness", self.best_fitness)

    def get_best_project(self):
        return self.best_project
