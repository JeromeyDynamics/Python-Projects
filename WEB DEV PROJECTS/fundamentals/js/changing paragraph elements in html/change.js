let name = "Jeromey Smol";
let age = 938254;
let student = true;

document.getElementById("p1").textContent = `Your name is ${name}`;
document.getElementById("p2").textContent = `Your ${age} years old`;
if (student == true) {
    document.getElementById("p3").textContent = `Your a student`;
} else {
    document.getElementById("p3").textContent = `Your not a student`;
}