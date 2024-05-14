//API to fetch historical data of Bitcoin Price Index
const api = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-31&end=2018-04-01';

/**
 * Loading data from API when DOM Content has been loaded'.
 * passes data to a function which will make the data suitable for line charts
 */
document.addEventListener("DOMContentLoaded", function(event) {
fetch(api)
    .then(function(response) { return response.json(); })
    .then(function(data) {
        var parsedData = parseData(data);
        //responsible for creating the line chart
        drawChart(parsedData);
    })
    .catch(function(err) { console.log(err); })
});

/**
 * Parse data into key-value pairs
 * @param {object} data Object containing historical data of BPI
 */
function parseData(data) {
    var arr = [];
    for (var i in data.bpi) {
        arr.push({
            date: new Date(i), //date
            value: +data.bpi[i] //convert string to number
        });
    }
    return arr;
}

/**
 * Creates a chart using D3
 * @param {object} data Object containing historical data of BPI
 */
function drawChart(data) {
    //defined variables for the line chart
    var svgWidth = 600, svgHeight = 400;
    var margin = { top: 20, right: 20, bottom: 30, left: 50 };
    var width = svgWidth - margin.left - margin.right;
    var height = svgHeight - margin.top - margin.bottom;

    //selects the svg element
    var svg = d3.select('svg')
        .attr("width", svgWidth)
        .attr("height", svgHeight);
    
    //appends a group tag inside the svg element
    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    //provides the scales for the line chart
    var x = d3.scaleTime()
        .rangeRound([0, width]);

    var y = d3.scaleLinear()
        .rangeRound([height, 0]);

    //creates the line
    var line = d3.line()
        //sets x
        .x(function(d) { return x(d.date)})
        //sets y
        .y(function(d) { return y(d.value)})
        //lets d3 know the scope of the data (returns the minimum and maximum)
        x.domain(d3.extent(data, function(d) { return d.date }));
        y.domain(d3.extent(data, function(d) { return d.value }));

    //appends group element
    g.append("g")
    //applies transformations
        .attr("transform", "translate(0," + height + ")")
        //calls d3.axisBottom on new element in line 63
        .call(d3.axisBottom(x))
        //removes all classes of domain
        .select(".domain")
        .remove();

    //appends group element
    g.append("g")
        //calls d3.axisLeft
        .call(d3.axisLeft(y))
        //apends some text
        .append("text")
        //applies elements to the text
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        //finds the end of y
        .attr("text-anchor", "end")
        //adds this text to the top of the y-axis
        .text("Price ($)");

    //appends path inside of a parent group element
    g.append("path")
        //apply the data set to datum
        .datum(data)
        //applies attributes to the path
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        //creates the line with the d attribute
        .attr("d", line);
}

