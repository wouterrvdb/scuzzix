# Imports
import math

from defaults import AMOUNT_OF_WORKERS


class ProjectComponent:
    # TODO: Add probability calculation

    def __init__(self, component_id, dependencies, topic, description, worker_times, project_manager_time,
                 material_cost):
        self.id = component_id
        self.dependencies = dependencies
        self.topic = topic
        self.description = description
        self.worker_times = worker_times
        self.project_manager_time = project_manager_time
        self.material_cost = material_cost
        self.assigned_workers = 1

    def fancy_print(self):
        print('ID: ', end='')
        print(self.id)
        print('Dependencies: ', end='')
        print(self.dependencies)
        print('Topic: ', end='')
        print(self.topic)
        print('Description: ', end='')
        print(self.description)
        print('Worker times: ', end='')
        print(self.worker_times)
        print('Project Manager time: ', end='')
        print(self.project_manager_time)
        print('Material Cost: ', end='')
        print(self.material_cost)
        print('Assigned amount of workers: ', end='')
        print(self.assigned_workers)
        print('Current duration: ', end='')
        print(self.get_duration())

    def get_duration(self):
        return max(self.worker_times[1] / self.assigned_workers, self.project_manager_time)

    def get_worker_time(self):
        return math.ceil(self.worker_times[1] / self.assigned_workers)

    def get_max_worker_time(self):
        return math.ceil(self.worker_times[2] / self.assigned_workers)

    def increase_workers(self, amount=1):
        self.assigned_workers += amount
        if self.assigned_workers > AMOUNT_OF_WORKERS:
            self.assigned_workers = AMOUNT_OF_WORKERS

    def decrease_workers(self, amount=1):
        self.assigned_workers -= amount
        if self.assigned_workers < 1:
            self.assigned_workers = 1

    def change_workers(self, amount):
        if amount < 1:
            self.assigned_workers = 1
        elif amount > AMOUNT_OF_WORKERS:
            self.assigned_workers = AMOUNT_OF_WORKERS
        else:
            self.assigned_workers = amount

    def get_minimum_duration(self):
        return min(min(self.worker_times), self.project_manager_time)

    def get_maximum_duration(self):
        return max(max(self.worker_times), self.project_manager_time)


class PlannedProjectComponent:
    def __init__(self, component, start_time, pessimistic=False):
        self.component = component
        self.start_time = start_time
        if pessimistic:
            self.end_time = math.ceil(self.start_time + self.component.get_maximum_duration())
        else:
            self.end_time = math.ceil(self.start_time + self.component.get_duration())

    def get_id(self):
        return self.component.id

    def fancy_print(self):
        self.component.fancy_print()
        print('Start time: ', end='')
        print(self.start_time)
        print('End time: ', end='')
        print(self.end_time)
        print()

    def get_planned_duration(self):
        return int(self.end_time - self.start_time)
