
// 7 tehtävä
const numDice = prompt("How many times would you like to throw dice?")

const diceNumb = [];

for (let i =1; i <= numDice; i+=1) {
  const dice = Math.random() * 6
  //console.log(dice)
  diceNumb.push(dice)

}

//console.log(diceNumb)

let sum = 0;

for (let i = 0; i < diceNumb.length; i++ ) {
  sum += diceNumb[i];
}
console.log("The sum of the dice is " + Math.round(sum))
document.querySelector("#teht7").innerHTML = "tehtävä 7 " + "The sum of the dice is " + Math.round(sum);



// 9 tehtävä
const num = prompt("Choose a whole number")

let isPrime = true

if (num <1) {
  isPrime = false
}
for (let i=2; i < num; i++) {
  if (num % i === 0) {
    isPrime = false
  }
}

console.log(isPrime)

document.querySelector("#teht9").innerHTML = "tehtävä 9 " + "is number " + num + " a prime number: " + isPrime;


