function afficherFormulaire(identification){
    for (let i = 0; i < tabBoutonPlusDansJour.length; i++) {
        tabBoutonPlusDansJour[i].addEventListener("click", ()=>{
            coteLabel.innerHTML = "";
            coteSelect.innerHTML = "";
            zoneformulaire.style.display = "block";
            formulaire(identification);
            
            // stockage de l'indice du bouton sur lequel l'utilisateur a cliqué
            const indice = i;
        }) 
    }
}

function autreFonction() {
    // accès à l'indice stocké précédemment
    console.log(indice);
}

autreFonction()