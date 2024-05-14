//javascript
//dataset for the bar chart
var dataset = [1, 2, 3, 4, 5];

//for width and height of svg container and the space between the bars
var svgWidth = 500, svgHeight = 300, barPadding = 5;
//calculates the width of each bar
var barWidth = (svgWidth / dataset.length);

//selects svg conatiner and gives it the variables created for width and height
var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);

//calls the function d3.scaleLinear which makes the bars scaled for the 
//visual representation so, a dataset with [5, 10, 15, 20] would be the same 
//height as a scale with the dataset [50, 100, 150, 200]
var yScale = d3.scaleLinear()
    //takes an array as an element
    .domain([0, d3.max(dataset)])
    //keeps the range of the scale in the svgContainer
    .range([0, svgHeight]);

//creates the bar chart, selects all rectangles/bars
var barChart = svg.selectAll("rect")
    //takes dataset into the waiting state
    .data(dataset)
    //takes the dataset from the waiting state into the doing stuff state
    //will call all further methods for each number in dataset
    .enter()
    //for each data item we will append a rectangle into the svg container
    .append("rect")
    //adds the y, height, width, and transform to each of the angles
    .attr("y", function(d) {
        return svgHeight - yScale(d);
    })
    .attr("height", function(d) { 
        return yScale(d);
    })
    .attr("width", barWidth - barPadding)
    .attr("transform", function (d, i) {
        //calculates level of translation for each bar on the x and y axis
        var translate = [barWidth * i, 0]; 
        return "translate("+ translate +")";
    });