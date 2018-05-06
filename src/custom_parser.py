import csv
from project_component import ProjectComponent


def parse(csv_path):
    counter = 0
    current_topic = ''
    component_list = []
    parsing = False
    with open(csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file, skipinitialspace=True)
        # Row is of the form "ID, Dependencies, Topic, Description, Min Time, Prob Time, Max Time, Time PM, Cost Materials"
        for row in reader:
            counter += 1
            # First row is just the header
            if counter is 1:
                continue
            # Some rows are just topics, cfr. "chapters" of the project
            if row[0] is '':
                current_topic = row[2]
                # Ignore the first project component
                if current_topic == "Measuring campaign":
                    parsing = True
                continue
            # Make the dependencies list empty if there are no dependencies
            dependencies = []
            if row[1] is not '':
                # Remove leading and trailing whitespace of dependencies
                dependencies = [string.strip() for string in row[1].split(',')]
            worker_times = [float(row[3]), float(row[4]), float(row[5])]
            project_manager_time = float(row[6])
            if parsing:
                component_list.append(ProjectComponent(component_id=str(row[0]),
                                                       dependencies=dependencies,
                                                       topic=current_topic,
                                                       description=row[2],
                                                       worker_times=worker_times,
                                                       project_manager_time=project_manager_time,
                                                       material_cost=0.0))  # TODO: Update costs
    return component_list
