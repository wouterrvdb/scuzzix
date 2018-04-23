import csv
from project_component import ProjectComponent


def parse(csv_path):
    counter = 0
    current_topic = ''
    component_list = []
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
                continue
            # Parse times from odd CSV layout to usable 2D matrix
            # TODO: clean up code (floats)
            times = [float(row[3])]
            selected_time = 0
            if float(row[4]) > float(row[3]):
                selected_time = 1
                times.append(float(row[4]))
            if float(row[5]) > float(row[4]):
                times.append(float(row[5]))
            times = [times, [float(row[6])]]
            selected_times = [selected_time, 0]
            component_list.append(ProjectComponent(component_id=row[0],
                                                   dependencies=row[1],
                                                   topic=current_topic,
                                                   description=row[2],
                                                   times=times,
                                                   selected_times=selected_times,
                                                   material_cost=0.0)) #TODO: Update costs
    return component_list
