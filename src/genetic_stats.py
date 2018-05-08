import math
import numpy as np
import pandas as pd
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


def plot_stats():
    fitness_history = _calc_fitness_history(_project_history)
    duration_history = _calc_duration_history(_project_history)

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

    dataframe = pd.DataFrame({
        "fitness": fitness_history,
        "duration": duration_history
    })

    dataframe.to_csv("genetic_algo_stats.csv")