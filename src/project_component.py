class ProjectComponent:

# TODO: Add probability calculation

    def __init__(self, component_id, dependencies, topic, description, worker_times, project_manager_time, material_cost):
        self.id = component_id
        self.dependencies = dependencies
        self.topic = topic
        self.description = description
        self.worker_times = worker_times
        self.project_manager_time = project_manager_time
        self.material_cost = material_cost
        self.assigned_workers = 0

    def fancy_print(self):
        print('ID: ', end='')
        print(self.id)
        print('Dependencies: ', end='')
        print(self.dependencies)
        print('Topic: ', end='')
        print(self.topic)
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
        if self.assigned_workers is 0:
            return None
        return max(self.worker_times[1]/self.assigned_workers, self.project_manager_time)

    def increase_workers(self):
        self.assigned_workers += 1

    def decrease_workers(self):
        if self.assigned_workers > 1:
            self.assigned_workers -= 1

    def change_workers(self, amount):
        self.assigned_workers += amount

    def initialize_task(self):
        self.assigned_workers = 1

    def get_minimum_duration(self):
        return min(min(self.worker_times), self.project_manager_time)

    def get_maximum_duration(self):
        return max(max(self.worker_times), self.project_manager_time)
