
const SEARCHAPIDiv = document.getElementById("SEARCHAPI");
const APIURLDiv = document.getElementById("APIURL");
const IMGPATHDiv = document.getElementById("IMGPATHDiv");
const corps = document.getElementById("corps");


const APIURL = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI = "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";




SEARCHAPIDiv.appendChild(SEARCHAPI);
APIURLDiv.appendChild(APIURL);
IMGPATHDiv.appendChild(IMGPATH);

corps.appendChild(SEARCHAPIDiv);
corps.appendChild(APIURLDiv);
corps.appendChild(IMGPATHDiv);
