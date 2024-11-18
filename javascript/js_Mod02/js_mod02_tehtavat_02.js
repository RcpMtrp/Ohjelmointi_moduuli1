"use strict"

// tehtävä 3
const namesList2 = document.querySelector("#ulist")
const names = []
let inner = ""


function asknames2() {
  for (let i = 0; i < 6; i++) {
    let name = prompt("Give a name for the dog")
    names.push(name)
  }
}

function printNames2() {

  for (let i = 0; i < names.length; i++) {
    names.sort().reverse()
    inner += `<li>${names[i]}</li>`
  }
  for (const name of names) {
    let liElement = document.createElement("li");
    liElement.innerHTML = name;
    namesList2.appendChild(liElement)
  }
}

asknames2()
printNames2()


// tehtävä 4
console.log("tehtävä4")

const numberList = []

let numbers = parseInt(prompt("Give a number"))
while (numbers !== 0){
  numberList.push(numbers)
  numbers = parseInt(prompt("Give a number"))
}

numberList.sort((a,b) => b-a)

console.log(numberList)



//tehtävä 5
console.log("tehtävä5")
const numbList = [];

function askNumber() {
  const numberQ = parseInt(prompt("Give a number:"));
  if(numbList.includes(numberQ)) {
    alert("This number has already been given. Stopping the program at once.")
    return;
  } else {
    numbList.push(numberQ);
    askNumber();
  }
}

askNumber();

numbList.sort((a,b) => a- b);

console.log(numbList);



// tehtävä 6

function rollDice () {
  return Math.floor(Math.random() * 6) +1;
}

function main() {
  const rollList = document.querySelector("#rolls");
  let roll;

  do {
    roll = rollDice();
    const li = document.createElement("li");
    li.textContent = `The rolled number is: ${roll}`;
    rollList.appendChild(li);
  } while (roll !== 6);
}

main();
