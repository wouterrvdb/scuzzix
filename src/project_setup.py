# Defaults

HOURS_PER_DAY = 8
WORKER_COST = 10
DAY_COST = 100


class Project:
    def __init__(self, components):
        self.components = components

    def init_components(self):
        for component in self.components:
            component.initialize_task()

    def calc_fitness(self):
        return 0

    def calc_min_fitness(self):
        duration = 0
        for component in self.project:
            duration += component.get_min_days()
        return duration

    def calc_max_fitness(self):
        days, cost = 0, 0
        for activity in self.project:
            days += activity.get_max_days()
            cost += activity.get_max_cost()
        return cost + days * DAY_COST
