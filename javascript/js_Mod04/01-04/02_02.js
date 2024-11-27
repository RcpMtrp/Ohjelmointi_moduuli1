"use strict"


 //const form = document.querySelector("form")
    //form.addEventListener('submit', function (event){
    document.querySelector("form").addEventListener('submit', function (event){
      console.log(event)
      event.preventDefault()
      const searchWord = document.getElementById("query").value
      console.log(searchWord)
      fetchTv(searchWord)
    })
    async function fetchTv(searchWord) {
      const response = await fetch(`https://api.tvmaze.com/search/shows?q=${searchWord}`)
      console.log(response)
      const data = await response.json()
      //console.log(data)
      createArticles(data)
    }

    function createArticles(data) {
      document.getElementById("results").innerHTML = ""
      console.log(data)
      for (const movie of data) {
        console.log(movie.show.name)

        const article = document.createElement("article")

        const h2 = document.createElement("h2")
        h2.innerText = movie.show.name

        const link = document.createElement("a")
        link.innerText = movie.show.url
        link.href = movie.show.url
        link.target = "_blank"

        const img = document.createElement("img")
        img.alt = movie.show.name
        //img.src = movie.show.image?.medium || "https://placedog.net/210/230"//"https://via.placeholder.com/210x295?text=Not%20Found"

/*
        if (movie.show.image) {
          img.src = movie.show.image.medium
        } else {
          img.src = "https://placedog.net/210/230"
        }
 */
        // ehto
        // ? arvo.JosOnTrue
        // : arvoJosOnFalse
        img.src = movie.show.image ? movie.show.image.medium : "https://placedog.net/210/230"

        const d = document.createElement("div")
        d.innerHTML = movie.show.summary

        article.appendChild(h2)
        article.appendChild(link)
        article.appendChild(img)
        article.appendChild(d)

        document.getElementById("results").appendChild(article)

      }
    }

