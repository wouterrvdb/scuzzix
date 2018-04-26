# Imports
import copy
import math
import sys

from project_component import PlannedProjectComponent
from resource_pool import ResourcePool

# Defaults

HOURS_PER_DAY = 8
HOUR_LIMIT = 2*30*HOURS_PER_DAY

AMOUNT_OF_PMS = 1
AMOUNT_OF_WORKERS = sys.maxsize


WORKER_COST = 10    # Cost for a worker each hour
DAY_COST = 100      # Cost for working an extra day


class Project:
    def __init__(self, components):
        self.components = copy.deepcopy(components)
        self.planning = []
        self.pm_pool = ResourcePool(AMOUNT_OF_PMS, HOUR_LIMIT)
        self.worker_pool = ResourcePool(AMOUNT_OF_WORKERS, HOUR_LIMIT)
        self._plan_components()

    def _plan_components(self):
        self.planning = []
        components = self.components[:]
        i = 0
        while len(components) is not 0:
            # print(i, '=', components[i].id)
            if i > len(components)-1:
                i = 0
            else:
                # Get latest end time of dependencies
                if len(components[i].dependencies) is not 0:
                    dependency_end_times = []
                    for planned_component in self.planning:
                        if planned_component.get_id() in components[i].dependencies:
                            dependency_end_times.append(planned_component.end_time)
                    # All dependencies have not been planned yet - stall
                    if len(dependency_end_times) < len(components[i].dependencies):
                        i += 1
                    else:
                        start_time = max(dependency_end_times)
                        self._plan_component_dtime(components[i], start_time)
                        components.pop(i)
                        i = 0
                # No dependencies
                else:
                    self._plan_component_dtime(components[i], 0)
                    components.pop(i)
                    i = 0

    # Plan a component given its earliest time determined by its dependencies
    def _plan_component_dtime(self, component, dtime):
        worker_time = self.worker_pool.get_earliest_time(dtime, component.assigned_workers, component.get_worker_time())
        pm_time = self.pm_pool.get_earliest_time(dtime, 1, component.project_manager_time)
        # print('Component', component.id, ':', pm_time, 'vs', worker_time)
        while pm_time != worker_time:
            if pm_time > worker_time:
                worker_time = self.worker_pool.get_earliest_time(pm_time, component.assigned_workers,
                                                                 component.get_worker_time())
            else:
                pm_time = self.pm_pool.get_earliest_time(worker_time, 1, component.project_manager_time)
        time = math.ceil(max(dtime, worker_time))
        self.worker_pool.allocate(time, component.assigned_workers, component.get_worker_time())
        self.pm_pool.allocate(time, 1, int(component.project_manager_time))
        self.planning.append(PlannedProjectComponent(component, time))

    def calc_fitness(self):
        worker_hours = 0
        for component in self.components:
            worker_hours += component.get_duration() * component.assigned_workers
        return self.get_duration()/HOURS_PER_DAY * DAY_COST + worker_hours * WORKER_COST

    def calc_min_fitness(self):
        hours = 0
        for component in self.components:
            hours += component.project_manager_time
        return hours / HOURS_PER_DAY * DAY_COST + hours * WORKER_COST

    def calc_max_fitness(self):
        worker_hours = 0
        for component in self.components:
            worker_hours += component.get_maximum_duration()
        return self.get_duration() / HOURS_PER_DAY * DAY_COST + worker_hours * WORKER_COST

    def get_duration(self):
        max_duration = 0
        for component in self.planning:
            max_duration = max(max_duration, component.end_time)
        return max_duration

    def print_planning(self):
        for component in self.planning:
            component.fancy_print()
