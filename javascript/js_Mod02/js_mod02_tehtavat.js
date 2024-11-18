"use strict"

// tehtävä 1
const numbers = []

for (let i = 0; i < 5; i++) {
  let numberPrompt = prompt("Anna numero:")
  numbers.unshift(numberPrompt)
}
console.log("tehtävä1", numbers)


// tehtävä 2

const namesList = document.querySelector("#namelist")
console.log(namesList)
const numParticipants = parseInt(prompt("Give a number of participants"))
const names = []
let inner = ""


function asknames() {
  for (let i = 0; i < numParticipants; i++) {
    console.log(i)
    let name = prompt("Give a name for the participant")
    names.push(name)
  }
  console.log(names)
}

function printNames() {
  // printataan konsoliin

  for (let i = 0; i < names.length; i++) {
    console.log(names[i])
    inner += `<li>${names[i]}</li>`
  }
  console.log(inner)
  //namesList.innerHTML = inner
  for (const name of names) {
    console.log(name)
    //inner += <li>${name}</li>
    let liElement = document.createElement("li");
    liElement.innerHTML = name;
    namesList.appendChild(liElement)
  }
}

asknames()
printNames()

/*
for (let i = 0; i < numParticipants; i++) {
  const names = prompt("Give a name of the participant:")
  namesList.unshift(names)
}
*/

document.querySelector("#olist").innerHTML = namesList
console.log(namesList)

