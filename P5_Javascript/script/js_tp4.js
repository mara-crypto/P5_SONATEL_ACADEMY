const zone = document.getElementById("zone");
let motDePasse = document.getElementById("motDePasse");
const number = document.getElementById("number");
const letMaj = document.getElementById("letMaj");
const letMin = document.getElementById('letMin');
const nombre = document.getElementById("nombre");
const speciaux = document.getElementById("speciaux");
const generer = document.getElementById("generer");

const Lettres_Maj = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
const Lettres_Min = 'abcdefghijklmnopqrstuvwxyz';
const Nombre = '0123456789';
const Caractere_Sp = '!@#$%&*()_+|}{[]\:;?><,./-=';

function genererMotDePasse (){

    let chaine = ""  
    let password = ""

    if (letMaj.checked) {
        chaine += letMaj
    }

    if (letMin.checked) {
        chaine += letMin
    }
    
    if (nombre.checked) {
        chaine += nombre
    }

    if (speciaux.checked) {
        chaine += speciaux
    }

    for ( let i=0; i<number.value; i++) {
        let index = Math.floor(Math.random()*chaine.length)
        password += chaine[index]
    }

    motDePasse.value = password
    
}

function activerBouton () {
    if (letMaj.checked || letMin.checked || nombre.checked || speciaux.checked) {
        generer.disabled = false ;
    }
    else{
        generer.disabled = true ;
    }
}

letMaj.addEventListener('change', activerBouton);
letMin.addEventListener("change", activerBouton);
nombre.addEventListener("change", activerBouton);
speciaux.addEventListener("change", activerBouton)
generer.addEventListener("click", genererMotDePasse)



