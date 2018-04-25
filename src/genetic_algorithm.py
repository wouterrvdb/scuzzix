# Imports
import random
import sys
import copy

from project_setup import Project


class GeneticAlgorithm:
    def __init__(self, components):
        self.components = components
        self.best_project = Project(self.components)
        self.best_fitness = self.best_project.calc_fitness()

        self.current_fitness = None
        self.min_fitness = self.best_project.calc_max_fitness()
        self.max_fitness = self.best_project.calc_min_fitness()

    def _crossbreed(self):
        pass

    def _mutate(self):
        '''prob = (current_fitness - min_fitness) / (max_fitness - min_fitness)
        for activity in setup:
            if random.random() <= prob:
                if random.random < 0.5:
                    activity.burn()
                else:
                    activity.non_burn()
        return setup'''
        pass

    def run(self, iterations):
        print("Base fitness: \t" + self.current_fitness)

        for i in range(0, iterations):
            self._mutate()
            self.current_fitness = self.components.calc_fitness()
            if self.current_fitness < self.best_fitness:
                self.best_components = copy.deepcopy(self.components)
                self.best_fitness = self.current_fitness
                print("New best fitness: \t" + self.best_fitness)

        return self.best_components
