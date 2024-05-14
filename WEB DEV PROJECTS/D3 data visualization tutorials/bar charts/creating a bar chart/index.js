//javascript
//dataset for the bar chart
var dataset = [80, 100, 56, 120, 180, 30, 40, 120, 160];

//for width and height of svg container and the space between the bars
var svgWidth = 500, svgHeight = 300, barPadding = 5;
//calculates the width of each bar
var barWidth = (svgWidth / dataset.length);

//selects svg conatiner and gives it the variables created for width and height
var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);
    
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
        return svgHeight - d ;
    })
    .attr("height", function(d) { 
        return d; 
    })
    .attr("width", barWidth - barPadding)
    .attr("transform", function (d, i) {
        //calculates level of translation for each bar on the x and y axis
        var translate = [barWidth * i, 0]; 
        return "translate("+ translate +")";
    });