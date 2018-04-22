const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
    input: fs.createReadStream(path.join(__dirname, '..', 'data', 'edited.tsv')),
    crlfDelay: Infinity
});

var linecounter = 0;
var to_write = `<html>
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
`;

function finish_writing(text) {
    return text + `      ]);

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
</html>`;
}

rl.on('line', (line) => {
    linecounter = linecounter + 1;
    var splitt = line.split("\t");
    if (linecounter == 1) {
        // Skip
    } else {
        to_write = to_write + "        ['"
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
        to_write = to_write + "],\n";
    }
    console.log(to_write);
}).on('close', () => {
    fs.writeFileSync(path.join(__dirname, '..', 'example', 'index.html'), finish_writing(to_write), function(err) {
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });
});
