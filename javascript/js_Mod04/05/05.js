"use strict"

async function getAJoke() {
  const outputElem = document.querySelector("#joke")
  const response = await fetch("https://api.chucknorris.io/jokes/random")
  const joke = await response.json()
  console.log("vitsi ", joke.value)
}
getAJoke()
