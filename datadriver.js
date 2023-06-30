console.log("fetching data");

fetch("/traveltime/traveltime.csv", { 
    method: 'GET'
})
    .then(function(response) { return response.text(); })
    .then(function(data) {
    console.log(data);

    // generate a table with data
    // console.log(parseCSV(data));
    console.log(data.split("\n")[0].split(","));
    var headers = data.split("\n")[0].split(",");

    var dataContainer = document.getElementById("data-container");
    // dataContainer.textContent = parseCSV(data);
    var datarows = data.split("\n");

    // table root
    var tableRoot = document.createElement("table");
    dataContainer.appendChild(tableRoot);

    for (var row = 0; row < datarows.length; row++) {
        var tablerow = document.createElement("tr");
        tableRoot.appendChild(tablerow);
        var datacols = datarows[row].split(",");
        if (row != 0) {
            for (var col = 0; col < datacols.length; col++) {
                var tablecol = document.createElement("td");
                tablerow.appendChild(tablecol);
                tablecol.textContent = datacols[col];
                if (col == 1) {
                    tablecol.style["color"]="#ff6666";
                }
                if (col == 4) {
                    tablecol.style["color"]="#6699ff";
                }
            }
        }
        else {
            for (var col = 0; col < datacols.length; col++) {
                var tablecol = document.createElement("th");
                tablerow.appendChild(tablecol);
                tablecol.textContent = datacols[col];
                if (col == 1) {
                    tablecol.style["color"]="#ffb3b3";
                }
                if (col == 4) {
                    tablecol.style["color"]="#b3ccff";
                }
            }
        }
    }
});

function parseCSV(data) {
    var lines=data.split("\n");

    var result = [];

    // NOTE: If your columns contain commas in their values, you'll need
    // to deal with those before doing the next step 
    // (you might convert them to &&& or something, then covert them back later)
    // jsfiddle showing the issue https://jsfiddle.net/
    var headers=lines[0].split(",");

    for(var i=1;i<lines.length;i++){

        var obj = {};
        var currentline=lines[i].split(",");

        for(var j=0;j<headers.length;j++){
            obj[headers[j]] = currentline[j];
        }

        result.push(obj);

    }

    //return result; //JavaScript object
    return JSON.stringify(result); //JSON
}