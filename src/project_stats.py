import pandas as pd

from matplotlib import pyplot as plot

from project_setup import Project

def plot_evolution_over_time(project: Project):
    workers_needed = [0 for _ in range(0, project.get_duration())]
    pms_needed = [0 for _ in range(0, project.get_duration())]

    total_workers_time = 0
    total_pm_time = 0

    for component in project.components:
        total_workers_time += component.worker_times[1]
        total_pm_time += component.project_manager_time

    for planned_component in project.planning:
        work = planned_component.component.worker_times[1]
        work_pm = planned_component.component.project_manager_time
        for t in range(planned_component.start_time, planned_component.end_time):
            assigned = (planned_component.component.assigned_workers
                        if work > planned_component.component.assigned_workers
                        else work)

            work -= assigned
            workers_needed[t] += assigned

            if work_pm > 0:
                work_pm -= 1
                pms_needed[t] += 1

            if work_pm == 0 and work == 0:
                break

    project_manager_burndown = [total_pm_time]
    workers_burndown = [total_workers_time]

    remaining_pm_time = total_pm_time
    remaining_workers_time = total_workers_time
    for t in range(0, project.get_duration()):
        remaining_workers_time -= workers_needed[t]
        remaining_pm_time -= pms_needed[t]

        workers_burndown.append(remaining_workers_time)
        project_manager_burndown.append(remaining_pm_time)


    plot.clf()
    plot.plot(workers_needed)
    plot.ylabel('Workers')
    plot.xlabel('Time [H]')
    plot.savefig('workers_time.png')

    plot.clf()
    plot.plot(workers_burndown)
    plot.ylabel('Remaining work (Workers)')
    plot.xlabel('Time [H]')
    plot.savefig('workers_burndown.png')

    plot.clf()
    plot.plot(project_manager_burndown)
    plot.ylabel('Remaining work (PM)')
    plot.xlabel('Time [H]')
    plot.savefig('pm_burndown.png')

    dataframe = pd.DataFrame({
        "workers": workers_needed,
        "workers_burndown": workers_burndown[:-1],
        "pm_burndown": project_manager_burndown[:-1]
    })

    dataframe.to_csv("project_progress.csv")

