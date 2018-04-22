# Imports
import random
import sys

# Defaults

DAY_COST = 100

# Globals

current_fitness = sys.maxsize
min_fitness = None
max_fitness = None


# Functions

def _calculate_fitness(setup):
    fitness = 0
    for activity in setup:
        fitness += activity.get_cost() + activity.get_days() * DAY_COST
    # TODO Add penalty for fluctuation
    return fitness


def _mutate(setup):
    prob = (current_fitness - min_fitness) / (max_fitness - min_fitness)
    for activity in setup:
        if random.random() <= prob:
            if random.random < 0.5:
                activity.burn()
            else:
                activity.non_burn()
    return setup


def _calculate_min_fitness(setup):
    days, cost = 0, 0
    for activity in setup:
        days += activity.get_min_days()
        cost += activity.get_min_cost()
    return cost + days * DAY_COST


def _calculate_max_fitness(setup):
    days, cost = 0, 0
    for activity in setup:
        days += activity.get_max_days()
        cost += activity.get_max_cost()
    return cost + days * DAY_COST


def init_fitnesses(setup):
    global current_fitness, min_fitness, max_fitness
    current_fitness = _calculate_fitness(setup)
    min_fitness = _calculate_min_fitness(setup)
    max_fitness = _calculate_max_fitness(setup)


def get_solution(current_setup, iterations):
    global current_fitness
    init_fitnesses(current_setup)
    best_setup = current_setup
    best_fitness = current_fitness
    print("Base fitness: \t" + current_fitness)

    for i in range(0, iterations):
        current_setup = _mutate(current_setup)
        current_fitness = _calculate_fitness(current_setup)
        if current_fitness < best_fitness:
            best_setup = current_setup[:]
            best_fitness = current_fitness
            print("New best fitness: \t" + best_fitness)

    return best_setup
