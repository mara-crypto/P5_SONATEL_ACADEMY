
const jour = document.getElementById("jour"); 
const heure = document.getElementById("heure"); 
const minute = document.getElementById("minute"); 
const seconde = document.getElementById("seconde"); 

function afficherCompteARebours () {

    let dateActuelle =  new Date();
    const date2024 = new Date("2024-01-01T00:00:00");
    let dureeRestantEnMillisecondes = date2024 - dateActuelle;

    let nombresDeJours = Math.floor(dureeRestantEnMillisecondes / (1000 * 60 * 60 *24));
    let nombresDeHeures = Math.floor((dureeRestantEnMillisecondes % (1000 * 60 * 60 *24)) / ( 1000 * 60 * 60));
    let nombresDeMinutes = Math.floor((dureeRestantEnMillisecondes % ( 1000 * 60 * 60)) / ( 1000 * 60 ));
    let nombresDeSeconde = Math.floor((dureeRestantEnMillisecondes % ( 1000 * 60 )) / 1000 );

    jour.innerText = `- ${nombresDeJours}` ;
    heure.innerText = `- ${nombresDeHeures}`;
    minute.innerText = `- ${nombresDeMinutes}`;
    seconde.innerText = `- ${nombresDeSeconde}`;



}

setInterval(afficherCompteARebours, 1000);