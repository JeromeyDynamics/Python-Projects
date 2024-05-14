// javascript

//creates variables
var svgWidth = 600, svgHeight = 500;
//selecs svg element
var svg = d3.select("svg")
    //gives width
    .attr("width", svgWidth)
    //gives height
    .attr("height", svgHeight)
    //used to let the css file give the box its orange color
    .attr("class", "svg-container")
    //gives the line its width
    .attr("stroke-width", 20);

//adds a line in the svg element (the orange box)
var line = svg.append("line")
    //gives the starting x
    .attr("x1", 100)
    //gives the ending x
    .attr("x2", 500)
    //gives the starting y
    .attr("y1", 50)
    //gives the ending y
    .attr("y2", 50)
    //give the line its color
    .attr("stroke", "red");

//adds a rectangle in the svg element
var rect = svg.append("rect")
    //provides the x and y points of the top left of the rectangle
    .attr("x", 200)
    .attr("y", 150)
    //provides the width and height starting from the top left
    //(x starts from the left and goes to the right why the y starts at 
    //the top and goes down)
    .attr("width", 250)
    .attr("height", 80)
    //gives the rectangle its color
    .attr("fill", "#9B95FF");

//adds a circle in the svg element
var circle = svg.append("circle")
    //x of the center of the circle
    .attr("cx", 200)
    //y of the center of the circle
    .attr("cy", 400)
    //the radius of the circle
    .attr("r", 100)
    //gives the circle its color
    .attr("fill", "#7CE8D5");
