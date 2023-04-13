const movieContainer = document.querySelector(".movies");


const APIURL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI = "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";


fetch(APIURL)
.then(reponse => reponse.json())
.then(data => console.log(data));

function remplissage(movie){
    const movieElement = document.createElement("div");
    movieElement.classList.add("movie");

    const moviePoster = document.createElement("img");
    moviePoster.classList.add("image");
    moviePoster.src = IMGPATH + movie.poster_path;
    moviePoster.alt = movie.title;

    const movieInfo = document.createElement("div");
    movieInfo.classList.add("movie-info");

    const movieTitle = document.createElement("h3");
    movieTitle.classList.add("movieTitle");
    movieTitle.textContent = movie.title;

    const movieRating = document.createElement("span")
    movieRating.classList.add('rating');
    movieRating.textContent = movie.vote_average;

    const movieRelease = document.createElement('p');
    movieRelease.classList.add("relase-date");
    movieRelease.textContent = movie.release_date;

    const movieDescription = document.createElement("p");
    movieDescription.classList.add('description');
    movieDescription.textContent = movie.overview;
    movieDescription.style.display= "none"

    const div = document.createElement("div")
    div.id = "classDiv";
    div.appendChild(moviePoster);
    div.appendChild(movieDescription);

    movieInfo.appendChild(movieTitle);
    movieInfo.appendChild(movieRating);
    movieInfo.appendChild(movieRelease);

    movieElement.appendChild(div);
    movieElement.appendChild(movieInfo);
    

    movieElement.addEventListener("mouseover", () => {
        movieDescription.style.display = "block";
        
        div.appendChild(movieDescription);
      });
      
      movieElement.addEventListener("mouseout", () => {
        movieDescription.style.display = "none";
        
        movieElement.removeChild(movieDescription);
      });
      

    movieContainer.appendChild(movieElement);
}

function affichermovie() {
    fetch(APIURL)
        .then(reponse => reponse.json())
        .then(data => {
            data.results.forEach(movie => {
                remplissage(movie)
            });
        })
}


affichermovie();

const searchInput = document.getElementById("searchInput");
const searchButton = document.getElementById("searchButton");

searchButton.addEventListener("click", () => {
  rechercheMovie()
})


function rechercheMovie (){
  fetch(APIURL)
  .then(reponse => reponse.json())
  .then(data => {
    movieContainer.innerHTML = "";
    data.results.forEach(movie => {
      if (searchInput.value === movie.title) {
        remplissage(movie)
      }
    })
  })

}

searchInput.addEventListener("input",() => {
    const valeur = searchInput.value.toLowerCase();
    valeur.toLowerCase()
    rechercheAutocompletion(valeur);
})

function rechercheAutocompletion (valeur) {
    fetch(APIURL)
    .then(reponse => reponse.json())
    .then(data => {
        movieContainer.innerHTML = "";
        data.results.forEach(movie =>{
            
            if (movie.title.toLowerCase().includes(valeur)) {
                remplissage(movie)

            }


        })
    })
}

