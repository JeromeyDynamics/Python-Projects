//javascript
//returns the first selection of the element matching the criteria
d3.select();
//returns all of the elements matching the criteria
d3.selectAll();
//makes words red
d3.select('h1').style('color', 'red')
//adds class or id to a method
.attr('class', 'heading')
//changes text
.text('new text');

//appended text to the body of the html file
//the append('p') meas that the .text() is as a paragraph
d3.select('body').append('p').text('first paragraph');
d3.select('body').append('p').text('second paragraph');
d3.select('body').append('p').text('third paragraph');

//vhanges all paragraphs to blue
d3.selectAll('p').style('color', 'blue');