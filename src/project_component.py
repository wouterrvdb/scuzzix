class ProjectComponent:

    def __init__(self, component_id, dependencies, topic, description, times, selected_times, material_cost):
        self.id = component_id
        self.dependencies = dependencies
        self.topic = topic
        self.description = description
        self.times = times  # 2D matrix, one dim. for all types of employees, one dim. for array of discrete times
        self.selected_times = selected_times
        self.material_cost = material_cost

    def fancy_print(self):
        print('ID: ', end='')
        print(self.id)
        print('Dependencies: ', end='')
        print(self.dependencies)
        print('Topic: ', end='')
        print(self.topic)
        print('Times: ', end='')
        print(self.times)
        print('Selected times: ', end='')
        print(self.selected_times)
        print('Material Cost: ', end='')
        print(self.material_cost)
