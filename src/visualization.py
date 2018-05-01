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
      data.addColumn('date', 'Start');
      data.addColumn('date', 'End');
      data.addColumn('number', 'Duration');
      data.addColumn('number', 'Percent Complete');
      data.addColumn('string', 'Dependencies');

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
    ''' to_write = to_write + "        ['"
        to_write = to_write + splitt[0];
        to_write = to_write + "', '";
        to_write = to_write + splitt[3];
        to_write = to_write + "', '";
        to_write = to_write + splitt[2];
        to_write = to_write + "', null, null, ";
        to_write = to_write + splitt[4];
        to_write = to_write + ", null, ";
        if (splitt[1] == "") {
            to_write = to_write + "null";
        } else {
            to_write = to_write + "'" + splitt[1] + "'";
        }
        to_write = to_write + "],\n";'''
    to_write = ""
    for planned_component in project.planning:
        to_write += "        ['"
        to_write += planned_component.component.id
        to_write += "', '"
        to_write += planned_component.component.description
        to_write += "', '"
        to_write += planned_component.component.topic
        to_write += "', null, null, "
        to_write += "{:.2f}".format(planned_component.component.get_duration()*24*60*60*1000)  # Round float to prevent issues
        to_write += ", null, "
        if not planned_component.component.dependencies:
            to_write += "null"
        else:
            to_write += "'" + ",".join(planned_component.component.dependencies) + "'"
        to_write += "],\n"
    return to_write
