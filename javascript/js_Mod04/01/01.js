"use strict"

async function fetchTv () {

  const response = await fetch("https://api.tvmaze.com/search/shows?q=girls")
  const query = await response.json();
  console.log(query.name);

}
fetchTv()

