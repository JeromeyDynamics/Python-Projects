//javascript
var dataset = [1, 2, 3, 4, 5];

//selects the body method of the html file
d3.select('body')
    //selects all paragraph text
    .selectAll('p')
    //puts the dataset in the waiting state for further processing
    .data(dataset)
    //takes data methods one by one and performs further operations on each
    .enter()
    //appends a paragraph text
    .append('p')
    //adds the stuff in the text parameters
    .text('D3 is awesome!');
    //takes each number in the dataset (use interchangably with the text above to change the text)
    //.text(function(d) { return d; });