// JSON = (JavaScript Object Notation) data-interchange format 
//                Used for exchanging data between a server and a web application
//                JSON files {key:value} OR [value1, value2, value3]

// JSON.stringify() = converts a JS object to a JSON string.
// JSON.parse() = converts a JSON string to a JS object

// ---------- JSON.stringify() ----------
//all of the stuff in here doesn't have to be in the json file
const names = ["Jimbob", "Jim", "Bob", "Jimmy"];
const snake = {
    "name": "Jimbob",
    "age": 65,
    "gay": false,
    "length in feet": 8,
    "food": ["mice", "nuts", "leaves"]
};
const snakes = [{
    "name": "Jimbob",
    "age": 65,
    "gay": false,
    "length in feet": 8,
    "food": ["mice", "nuts", "leaves"]
},
{
    "name": "Jim",
    "age": 2,
    "gay": false,
    "length in feet": 2,
    "food": ["milk", "nut"]
},
{
    "name": "Bob",
    "age": 2628618,
    "gay": true,
    "length in feet": 83748946.45,
    "food": ["supermassive black hole", "super clusters", "milkyway galaxy"]
},
{
    "name": "Jimmy",
    "age": 18,
    "gay": false,
    "length in feet": 0.0001,
    "food": ["half an atom"]
}]

console.log("Stringify:\n");

const jsonString1 = JSON.stringify(names);
console.log("the names of the snakes:\n\n" + jsonString1);

const jsonString2 = JSON.stringify(snake);
console.log("one of the snakes:\n\n" + jsonString2);

const jsonString3 = JSON.stringify(snakes);
console.log("all of the snakes:\n\n" + jsonString3);

// ---------- JSON.parse() ----------

const jsonNames = `["Jimbob", "Jim", "Bob", "Jimmy"]`;
const jsonSnake = `{ "name": "Jimbob", "age": 65, "gay": false, "length in feet": 8, "food": ["mice", "nuts", "leaves"]}`;
const jsonSnakes = 
`[{
    "name": "Jimbob",
    "age": 65,
    "gay": false,
    "length in feet": 8,
    "food": ["mice", "nuts", "leaves"]
},
{
    "name": "Jim",
    "age": 2,
    "gay": false,
    "length in feet": 2,
    "food": ["milk", "nut"]
},
{
    "name": "Bob",
    "age": 2628618,
    "gay": true,
    "length in feet": 83748946.45,
    "food": ["supermassive black hole", "super clusters", "milkyway galaxy"]
},
{
    "name": "Jimmy",
    "age": 18,
    "gay": false,
    "length in feet": 0.0001,
    "food": ["half an atom"]
}]`;


console.log("Parse:\n");

const parsedData1 = JSON.parse(jsonNames);
console.log("parsed names:\n\n" + parsedData1);

const parsedData2 = JSON.parse(jsonSnake);
console.log("parsed snake:\n\n" + parsedData2);

const parsedData3 = JSON.parse(jsonSnakes);
console.log("parsed snakes:\n\n" + parsedData3);

// ---------- fetch() ----------
fetch("C:/Users/Omega/epic_stuff/WEB DEV PROJECTS/Bro Code/using JSON files/snakes.json")
    .then(response => response.json())
    .then(values => values.forEach(value => console.log(value)))
    .catch(error => console.error(error));