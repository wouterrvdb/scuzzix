# Imports
import random
import sys
import copy

import stats

from project_setup import Project


class GeneticAlgorithm:
    def __init__(self, components):
        self.components = components

        self.best_project = Project(self.components)
        self.best_fitness = self.best_project.calc_fitness()

        self.current_fitness = self.best_fitness

        self.min_fitness = self.best_project.calc_max_fitness()
        self.max_fitness = self.best_project.calc_min_fitness()

    def _crossbreed(self):
        new_components = []
        prob = (self.best_fitness - self.min_fitness) / (self.max_fitness - self.min_fitness)
        for i in range(0, len(self.components)):
            if random.random() > prob:
                new_components.append(self.best_project.components[i])
            else:
                new_components.append(self.components[i])
        self.components = new_components

    def _mutate(self):
        prob = (self.current_fitness - self.min_fitness) / (self.max_fitness - self.min_fitness)
        for component in self.components:
            if random.random() < prob:
                if random.random() > 0.5:
                    component.increase_workers()
                else:
                    component.decrease_workers()

    def run(self, iterations):
        print("Running genetic algorithm for", iterations, "iterations...")
        print("Start fitness", self.current_fitness)
        for i in range(0, iterations):
            self._crossbreed()
            self._mutate()

            current_project = Project(self.components)
            self.current_fitness = current_project.calc_fitness()

            stats.log_stats(current_project)

            if self.current_fitness < self.best_fitness:
                self.best_project = Project(self.components)
                self.best_fitness = self.current_fitness
        stats.plot_stats()
        print("End fitness", self.best_fitness)
