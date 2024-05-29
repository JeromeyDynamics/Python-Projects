//hiding all elements off the start
document.getElementById("secondaryButtons").style.display = "none";

//gets geometry button element
const geoB = document.getElementById("geometryButton");

//function for clicking the button
geoB.addEventListener("click", function(e) {
    document.getElementById("primaryButtons").style.display = "none";
    console.log("geometry button pressed!");
});

//gets geometry button element
const pythagB = document.getElementById("pythagoreanButton");

//function for clicking the button
pythagB.addEventListener("click", function(e) {
    document.getElementById("primaryButtons").style.display = "none";
    document.getElementById("pythagoreanStuff").style.display = "run-in";
    console.log(document.getElementById("pythagoreanStuff").style.display);
    console.log("pythagorean button pressed!");
});

//gets geometry button element
const algeB = document.getElementById("algebraButton");

//function for clicking the button
algeB.addEventListener("click", function(e) {
    document.getElementById("primaryButtons").style.display = "none";
    console.log("algebra button pressed!");
});

//gets go home button element
const homeB = document.getElementById("homeButton");

//function for clicking the button
homeB.addEventListener("click", function(e) {
    document.getElementById("secondaryButtons").style.display = "none";
    document.getElementById("primaryButtons").style.display = "initial";
    console.log("home button pressed!");
});