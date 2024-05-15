// javascript

//creates data array
var data= [80, 100, 56, 120, 180, 30, 40, 120, 160];

//creates the height and widh of the axes
var svgWidth = 500, svgHeight = 300;

//uses the height and width given for the axes
var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);

//creates the scales for the axes
var xScale = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, svgWidth]);

var yScale = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([svgHeight, 0]);

//creates axes using the scales created earlier
var x_axis = d3.axisBottom()
    .scale(xScale);

var y_axis = d3.axisLeft()
    .scale(yScale);

//appends a group element inside of the svg element for the y-axis
svg.append("g")
    .attr("transform", "translate(50, 10)")
    .call(y_axis);
    
var xAxisTranslate = svgHeight - 20;
//appends a group element inside of the svg element for the x-axis

svg.append("g")
    .attr("transform", "translate(50, " + xAxisTranslate  +")")
    .call(x_axis);