//don't actually need the semicolons at the end of most lines
//accept for special occurances but, its good to put them there
//incase of an error being thrownfor not having it
let age = 14;
let strength = 1536; //weight to curl
let speed = 7352; //max mph/2
let totalMoney = -3;

let firstName = 'Jerome'
let lastName = 'Hillock'

let online = true

//doesn't matter if it has single or double quotes and the ` symbols 
//acts to add variable
console.log(`You are ${age} years old and probably in grades ${age-6}-${age-5}`);

if ((strength + speed) > 30) {
    console.log("You are superhuman :)");
} else {
    console.log('You aren\'t superhuman :(');
}
if (totalMoney > 0) {
    console.log(`You have $${totalMoney} left in your bank account :)`);
} else {
    console.log(`You have -$${Math.abs(totalMoney)} left in your bank account :(`);
}

console.log('----------------------------------------------');

console.log("the value of the age variable is " + typeof age);
console.log(firstName + " " + lastName + ` is online: ${online}`);