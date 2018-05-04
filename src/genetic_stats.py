import math
import numpy as np
from matplotlib import pyplot as plot

from project_setup import Project, HOURS_PER_DAY, WORKER_COST

_project_history = []


def log_stats(project: Project):
    _project_history.append(project)


def _calc_fitness_history(project_history):
    fitness = []

    for project in project_history:
        fitness.append(project.calc_fitness())

    return np.array(fitness)


def _calc_duration_history(project_history):
    duration = []

    for project in project_history:
        duration.append(math.ceil(project.get_duration() / HOURS_PER_DAY))

    return np.array(duration)

def _calc_cost_duration(project_history, max_duration):
    indexes = np.arange(max_duration + 1)
    cost_worker = [[] for _ in indexes]

    for project in project_history:
        cost = 0

        for component in project.components:
            cost += component.get_worker_time() * WORKER_COST

        cost_worker[math.ceil(project.get_duration() / HOURS_PER_DAY)].append(cost)

    r = np.column_stack((
        indexes,
        np.array([np.average(cost_worker[i]) for i in range(len(cost_worker))])
    ))

    return r[~np.isnan(r).any(axis=1)]

def plot_stats():
    fitness_history = _calc_fitness_history(_project_history)
    duration_history = _calc_duration_history(_project_history)

    cost_worker = _calc_cost_duration(_project_history, np.max(duration_history))

    plot.clf()
    plot.plot(fitness_history)
    plot.ylabel('Fitness')
    plot.xlabel('Iteration')
    plot.savefig('fitness_iteration.png')

    plot.clf()
    plot.plot(duration_history)
    plot.ylabel('Duration')
    plot.xlabel('Iteration')
    plot.savefig('duration_iteration.png')

    plot.clf()
    plot.plot(cost_worker[:, 0], cost_worker[:, 1], 'ro')
    plot.ylabel('Worker cost')
    plot.xlabel('Duration')
    plot.savefig('worker_cost_duration.png')