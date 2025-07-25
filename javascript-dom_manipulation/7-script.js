document.addEventListener("DOMContentLoaded", function() {
    fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
      .then(response => response.json())
      .then(data => {
        const movies = data.results;
        const listMovies = document.getElementById("list_movies");
        movies.forEach(movies => {
          const listItem = document.createElement("li");
          listItem.textContent = movies.title;
          listMovies.appendChild(listItem);
        })
      })
      .catch(error => console.error('Error', error));
});
