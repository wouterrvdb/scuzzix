from project_setup import Project

begin_string = '''<html>
<head>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
  <script type="text/javascript">
    google.charts.load('current', {'packages':['gantt']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Task ID');
      data.addColumn('string', 'Task Name');
      data.addColumn('string', 'Resource');
      data.addColumn('date', 'Start Date');
      data.addColumn('date', 'End Date');
      data.addColumn('number', 'Duration');
      data.addColumn('number', 'Percent Complete');
      data.addColumn('string', 'Dependencies');

      var start_date = new Date(2018, 8, 1)

      data.addRows([
'''

end_string = '''      ]);

      var options = {
        height: 5000,
        defaultStartDateMillis: new Date(2018, 8, 1)
      };

      var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

      chart.draw(data, options);
    }
  </script>
</head>
<body>
  <div id="chart_div"></div>
</body>
</html>'''


def visualize(project: Project, visualization_path):
    to_write = ""
    to_write += begin_string
    to_write += parse_project(project)
    to_write += end_string
    with open(visualization_path, mode='w', newline='') as visualization_file:
        visualization_file.write(to_write)


def parse_project(project: Project):
    # Row is of the form "ID, Dependencies, Topic, Description, Min Time, Prob Time, Max Time, Time PM, Cost Materials"
    to_write = ""
    for planned_component in project.planning:
        to_write += "        ['"
        to_write += planned_component.component.id
        to_write += "', '"
        to_write += planned_component.component.description
        to_write += "', '"
        to_write += planned_component.component.topic
        to_write += "', new Date("
        to_write += "start_date.getTime()+{0}*60*60*1000".format(planned_component.start_time)
        to_write += "), new Date("
        to_write += "start_date.getTime()+{0}*60*60*1000".format(planned_component.end_time)
        to_write += "), null, null, "
        if not planned_component.component.dependencies:
            to_write += "null"
        else:
            to_write += "'" + ",".join(planned_component.component.dependencies) + "'"
        to_write += "],\n"
    return to_write
