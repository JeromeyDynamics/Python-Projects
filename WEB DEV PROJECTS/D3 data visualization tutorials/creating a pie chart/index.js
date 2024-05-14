// javascript
//creates a dataset
var data = [
    {"platform": "Android", "percentage": 40.11}, 
    {"platform": "Windows", "percentage": 36.69},
    {"platform": "iOS", "percentage": 13.06}
];

//variable creation
var svgWidth = 500, svgHeight = 300, radius =  Math.min(svgWidth, svgHeight) / 2;
//selects the svg element and gves it the width and height
var svg = d3.select('svg')
    .attr("width", svgWidth)
    .attr("height", svgHeight);

//Create group element to hold pie chart    
var g = svg.append("g")
    .attr("transform", "translate(" + radius + "," + radius + ")") ;

//selects the range of colors for the pies of the chart
var color = d3.scaleOrdinal(d3.schemeCategory10);

//prepares data to be put in the pie chart
var pie = d3.pie().value(function(d) { 
     return d.percentage; 
});

//creates path elements using the path data
var path = d3.arc()
    //defines the boundaries of the arcs
    .outerRadius(radius)
    .innerRadius(0);
 
//creates arc
    var arc = g.selectAll("arc")
    .data(pie(data))
    .enter()
    .append("g");

//makes path
arc.append("path")
    .attr("d", path)
    .attr("fill", function(d) { return color(d.data.percentage); });

//lines in between each pie slice
var label = d3.arc()
    .outerRadius(radius)
    .innerRadius(0);
            
//puts text in each slice of the pie
    arc.append("text")
    .attr("transform", function(d) { 
        return "translate(" + label.centroid(d) + ")"; 
    })
    .attr("text-anchor", "middle")
    .text(function(d) { return d.data.platform+":"+d.data.percentage+"%"; });