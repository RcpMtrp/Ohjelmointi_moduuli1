
console.log("I'm printing to console!")


// 2 tehtävä

const nameInput = prompt("what is your name?")
console.log("Hello, " + nameInput + "!")

document.querySelector("#teht2").innerHTML = "tehtävä 2 " + "Hello, " + nameInput + "!";


// 3 tehtävä

const input1 = prompt("Anna luku 1.")
const input1Int = parseInt(input1)
const input2 = prompt("Anna luku 2.")
const input2Int = parseInt(input2)
const input3 = prompt("Anna luku 3.")
const input3Int = parseInt(input3)
const sum = input1Int + input2Int + input3Int
const avg = sum / 3

console.log("The sum of the numbers is: " + sum + ", the average of the numbers is: " + avg)

document.querySelector("#teht3").innerHTML = "tehtävä 3 " + "The sum of the numbers is: " + sum + ", the average of the numbers is: " + avg;




// 4 tehtävä

const name = prompt("What is your name?")
const randomNumber = Math.random() * 4
let hogwartsClass = ""

if (randomNumber >= 3) {
  hogwartsClass = "Gryffindor"
  //console.log(name + ", you are in Gryffindor")
} else if (randomNumber >=2) {
  hogwartsClass = "Slytherin"
  //console.log(name + ", you are in Slytherin")
} else if (randomNumber >=1) {
  hogwartsClass = "Hufflepuff"
  //console.log(name + ", you are in Hufflepuff")
} else {
  hogwartsClass = "Ravenclaw"
  //console.log(name + ", you are in Ravenclaw")
}
console.log(hogwartsClass)
document.querySelector("#teht4").innerHTML = "tehtävä 4 " + name + "you are in " + hogwartsClass + ".";



// 5 tehtävä

const yearStr = prompt("Give a year to check if it is a leap year")
const year = parseInt(yearStr)
isLeap = ""
if ((year % 400 == 0) || ((year % 100 != 0) && (year % 4 == 0))){
  isLeap = " is a leap year"
  //console.log(year + " is a leap year")
}
else {
  isLeap = " is not a leap year"
  // console.log(year + " is not a leap year")
}
document.querySelector("#teht5").innerHTML = "tehtävä 5 " + year + isLeap;





