const readline = require('readline');
const fs = require('fs');
const path = require('path');

const rl = readline.createInterface({
    input: fs.createReadStream(path.join(__dirname, '..', 'data', 'unedited.tsv')),
    crlfDelay: Infinity
});

function time_to_milliseconds(hours) {
    return hours*60*60*1000;
}

var linecounter = 0;
var to_write = "";
var current_group = "";
rl.on('line', (line) => {
    linecounter = linecounter + 1;
    var splitt = line.split("\t");
    if (linecounter == 1) {
        to_write = to_write + "ID";
        to_write = to_write + "\t";
        to_write = to_write + "Dependencies";
        to_write = to_write + "\t";
        to_write = to_write + "Group";
        to_write = to_write + "\t";
        to_write = to_write + "Task";
        to_write = to_write + "\t";
        to_write = to_write + "Time";
        to_write = to_write + "\n";
    } else {
        // Group split
        if (splitt[0] == "") {
            current_group = splitt[2];
        } else {
            to_write = to_write + splitt[0];
            to_write = to_write + "\t";
            to_write = to_write + splitt[1].replace(/ /g, "");
            to_write = to_write + "\t";
            to_write = to_write + current_group;
            to_write = to_write + "\t";
            to_write = to_write + splitt[2];
            to_write = to_write + "\t";
            to_write = to_write + time_to_milliseconds(splitt[4]);
            to_write = to_write + "\n";
        }
    }
    console.log(to_write);
}).on('close', () => {
    fs.writeFileSync(path.join(__dirname, '..', 'data', 'edited.tsv'), to_write, function(err) {
        if(err) {
            return console.log(err);
        }

        console.log("The file was saved!");
    });
});
