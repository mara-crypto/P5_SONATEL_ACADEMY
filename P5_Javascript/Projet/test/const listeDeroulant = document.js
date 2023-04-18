const listeDeroulant = document.getElementById("listeDeroulant") ;
const enseignantsDiv = document.getElementById("enseignant");
const sallesDiv = document.getElementById("salle");
const modulesDiv = document.getElementById("module");
const classesDiv = document.getElementById("classe");

const lundi = document.getElementById("element1");
const mardi = document.getElementById("element2");
const mercredi = document.getElementById("element3");
const jeudi = document.getElementById("element4");
const vendredi = document.getElementById("element5");
const samedi = document.getElementById("element6");

const ajouterDansLundi    = document.getElementById("ajouterDansLundi")
const ajouterDansMardi    = document.getElementById("ajouterDansMardi")
const ajouterDansMercredi = document.getElementById("ajouterDansMercredi")
const ajouterDansJeudi    = document.getElementById("ajouterDansJeudi")
const ajouterDansVendredi = document.getElementById("ajouterDansVendredi")
const ajouterDansSamedi   = document.getElementById("ajouterDansSamedi")

const affichePlaning = document.getElementById("affichePlaning")
const enseignants = [{nom: "Enseignants", id: "100", module:["300"]}, 
                     {nom: "Aly", id: "101", module:["305","306"]}, 
                     {nom: "Baila", id: "102", module:["305","306"]}, 
                     {nom: "Ndoye", id: "103", module:["305","306"]},
                     {nom: "Mbaye", id: "104", module:["302","303","301"]},
                     {nom: "Djiby", id: "105", module:["304"]}, 
                     {nom: "Seckouba", id: "106", module:["304","301"]}];

const classes = [{nom: "Classes", id: "200", nbrEleve: "00", salle:["00"]}, 
                {nom: "L2 GLRS A", id: "201", nbrEleve: "23", salle:["401","402","403","404","405","406"]}, 
                {nom: "L2 GLRS B", id: "202", nbrEleve: "25", salle:["401","402","403","404","405","406"]},
                {nom: "L2 ETSE", id: "203", nbrEleve: "30", salle:["403","404","405","406"]}, 
                {nom: "L1 A", id: "204", nbrEleve: "29", salle:["403","404","405","406"]},
                {nom: "IAGE B", id: "205", nbrEleve: "35", salle:["404"]},
                {nom: "L2 CDSD", id: "206", nbrEleve: "28", salle:["403","404","405","406"]}];

const modules = [{nom: "Modules", id: "300"}, 
                {nom: "ALGO", id: "301"}, 
                {nom: "PYTHON", id: "302"}, 
                {nom: "PHP", id: "303"}, 
                {nom: "LC", id: "304"}, 
                {nom: "JAVASCRIPT", id: "305"}, 
                {nom: "JAVA", id: "306"}];

const salles = [{nom: "Salles", id: "400", effectif: "00"}, 
                {nom: "101", id: "401", effectif: "25"},
                {nom: "102", id: "402", effectif: "25"},
                {nom: "103", id: "403", effectif: "30"},
                {nom: "104", id: "404", effectif: "35"}, 
                {nom: "201", id: "405", effectif: "30"}, 
                {nom: "incub", id: "406", effectif: "30"}];

const HeureDebuts = [{nom: "heure", id:"500"},
                     {nom: "8",  id:"501"},
                     {nom: "9",  id:"502"},
                     {nom: "10", id:"503"},
                     {nom: "11", id:"504"},
                     {nom: "12", id:"506"},
                     {nom: "13", id:"507"},
                     {nom: "15", id:"508"},
                     {nom: "16", id:"509"},
                     {nom: "17", id:"510"}]
                
const tabLabbel = ["Enseignant", "Module", "Salle","Classe", "HeureDebut", "HeureFin"];
const jours = [lundi, mardi, mercredi, jeudi, vendredi, samedi];
const tabBoutonPlusDansJour = [ajouterDansLundi, ajouterDansMardi, ajouterDansMercredi, ajouterDansJeudi, ajouterDansVendredi, ajouterDansSamedi]


const cours = [{Enseign: "101",
                Module: "305",
                Salle: "401",
                Classe: "206",
                HeureDebut: "8",
                HeureFin: "10",
                jour:"1" },

                {Enseign: "101",
                Module: "306",
                Salle: "401",
                Classe: "201",
                HeureDebut: "14",
                HeureFin: "17",
                jour: "2"},

                {Enseign: "104",
                Module: "302",
                Salle: "403",
                Classe: "203",
                HeureDebut: "9",
                HeureFin: "12",
                jour: "2"},

                {
                    Enseign: "105",
                    Module: "304",
                    Salle: "405",
                    Classe: "204",
                    HeureDebut: "13",
                    HeureFin: "15",
                    jour: "3"
                },

                {Enseign: "106",
                Module: "301",
                Salle: "403",
                Classe: "203",
                HeureDebut: "14",
                HeureFin: "16",
                jour: "4"}
            ]
    

const tabclassEnseiSalClassMod = document.querySelectorAll(".classEnseiSalClassMod ");
function m(){
    tabclassEnseiSalClassMod.forEach(elementTab => {
        elementTab.addEventListener("click", (event) => {
            const identifiant = (event.target.getAttribute("id"))
            if (identifiant === "enseignant"){
                creationlisteDeroulant(enseignants)
                enseignantsDiv.style.backgroundColor = "rgb(0, 166, 255)";
                classesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                modulesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                sallesDiv.style.backgroundColor = "rgba(154,154,154,255)";

            }
            if (identifiant === "classe"){
                creationlisteDeroulant(classes)
                classesDiv.style.backgroundColor = "orange"
                modulesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                sallesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                enseignantsDiv.style.backgroundColor = "rgba(154,154,154,255)";
            }
            if (identifiant === "module"){
                creationlisteDeroulant(modules)
                modulesDiv.style.backgroundColor = "red"
                sallesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                enseignantsDiv.style.backgroundColor = "rgba(154,154,154,255)";
                classesDiv.style.backgroundColor = "rgba(154,154,154,255)";
            }
            if (identifiant === "salle"){
                creationlisteDeroulant(salles)
                sallesDiv.style.backgroundColor = " rgb(6, 151, 6)"
                enseignantsDiv.style.backgroundColor = "rgba(154,154,154,255)";
                classesDiv.style.backgroundColor = "rgba(154,154,154,255)";
                modulesDiv.style.backgroundColor = "rgba(154,154,154,255)";
            }
})
}
)}
m()

function creationlisteDeroulant(tableau) {
    listeDeroulant.innerHTML = "";
    tableau.forEach(eltTableau => {
            let option = document.createElement("option");
            option.setAttribute("value",eltTableau.id)
            option.text = eltTableau.nom;
            listeDeroulant.appendChild(option);
    });
}

function recuperationNom(tableau){
    tableau.forEach(element => {
        const idelement = element.nom
    })
    
}




function planning(id, cours){
    if (enseignants.find(nomEnseign => nomEnseign.id === id)){
       
        var objets = cours.filter(nomClasse => nomClasse.Enseign === id )
    }
    if  (classes.find(nomClasse => nomClasse.id === id)){
        var objets = cours.filter(nomClasse => nomClasse.Classe === id )
    }
    if  (modules.find(nomModule => nomModule.id === id)){
        var objets = cours.filter(nomClasse => nomClasse.Module === id )
    }
    if  (salles.find(nomSalle => nomSalle.id === id)){
        var objets = cours.filter(nomClasse => nomClasse.Salle === id )
    }
   


    objets.forEach(objet => {
        const Classe = classes.find(nomClasse => nomClasse.id === objet.Classe).nom ;
        const Module = modules.find(nomModule => nomModule.id === objet.Module).nom ;
        const Enseign = enseignants.find(nomEnseign => nomEnseign.id === objet.Enseign).nom ;
        const Salle = salles.find(nomSalle => nomSalle.id ===  objet.Salle).nom ;
        const HeureDebut = objet.HeureDebut ;
        const HeureFin = objet.HeureFin ;
        const jour = objet.jour;
        
        const duree = HeureFin - HeureDebut;
        const marge = HeureDebut - 8
        let horair = document.createElement("div");

        if (enseignants.find(nomEnseign => nomEnseign.id === id)){
            jours.forEach(elementJour =>{
                if (elementJour == jours[jour-1]){
                    horair.innerHTML = "";
                    horair.innerHTML += `<p>${Classe}<br>${Module}<br>${Salle}</p>`;
                    elementJour.appendChild(horair);
                }
            })
        }
        if  (classes.find(nomClasse => nomClasse.id === id)){
            jours.forEach(elementJour =>{
                if (elementJour == jours[jour-1]){
                    horair.innerHTML = "";
                    horair.innerHTML += `<p>${Enseign}<br>${Module}<br>${Salle}</p>`;
                    elementJour.appendChild(horair);           
                }
            })
        }
        if  (modules.find(nomModule => nomModule.id === id)){
            jours.forEach(elementJour =>{
                if (elementJour == jours[jour-1]){
                    horair.innerHTML = "";
                    horair.innerHTML += `<p>${Enseign}<br>${Classe}<br>${Salle}</p>`;
                    elementJour.appendChild(horair);           
                }
            })
        }
        if  (salles.find(nomSalle => nomSalle.id === id)){
            jours.forEach(elementJour =>{
                if (elementJour == jours[jour-1]){
                    horair.innerHTML = "";
                    horair.innerHTML += `<p>${Enseign}<br><br>${Module}<br><br>${Classe}</p>`;
                    elementJour.appendChild(horair);           
                }
            })
        }
        if (duree === 1){
            horair.style.backgroundColor = "rgba(121, 15, 98, 0.925)";
        }
        if (duree === 2){
            horair.style.backgroundColor = "rgba(189, 0, 148, 0.925)";
        }
        if (duree === 3){
            horair.style.backgroundColor = "rgba(4, 172, 135, 0.925)";
        }
        if (duree === 4){
            horair.style.backgroundColor = "rgba(67, 127, 216, 0.925)";
        }
        if (duree === 5){
            horair.style.backgroundColor = "rgba(5, 32, 71, 0.925)";
        }
        if (duree > 6){
            horair.style.backgroundColor = "rgb(255, 187, 61)";
        }
        horair.style.marginLeft = `${marge*10}%`;
        horair.style.width = `${duree*10}%`;
        horair.style.height = "110px";
        horair.style.borderRadius = "15px"
        horair.style.display = "flex";
        horair.style.alignItems = "center";
        horair.style.textAlign = "center";
        horair.style.justifyContent = "center";
        horair.style.flexDirection = "column";
        horair.style.fontSize = "15px";
        horair.style.color = "white";
       
    })
}



const zoneformulaire = document.getElementById("zoneformulaire");
const header = document.createElement("header")
header.id = "header"
zoneformulaire.appendChild(header);
const form = document.createElement("form");
form.id = "form"
zoneformulaire.appendChild(form);
const footer = document.createElement("footer")
footer.id = "footer"
footer.style.display = "flex"
footer.style.justifyContent = "center"
footer.style.alignItems = "center"
zoneformulaire.appendChild(footer)

const coteLabel = document.createElement("div")
coteLabel.id ="coteLabel"
form.appendChild(coteLabel)
const coteSelect = document.createElement("div")
coteSelect.id = "coteSelect"
form.appendChild(coteSelect)

const ajouter = document.createElement("button");
ajouter.innerHTML = "Ajouter";
ajouter.style.height = "30px"
footer.appendChild(ajouter)

const annuler = document.createElement("button");
annuler.innerHTML = "Annuler";
annuler.style.height = "30px"
footer.appendChild(annuler)

function formulaire(identification, indice, valeur){
    tabLabbel.forEach(valeurLabel =>{
        
        if (valeurLabel === "Enseignant" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            let select = document.createElement("select");
            select.id = "select"
            label.innerHTML = valeurLabel
            creationlisteDeroulantFormulaire(enseignants, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);
        }
        if (valeurLabel === "Module" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            label.innerHTML = valeurLabel
            const select = document.createElement("select");
            select.id = "select"
            creationlisteDeroulantFormulaire(modules, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);

            select.addEventListener('change', function() {
                const option = select.options[select.selectedIndex];
                const item = {
                  id: option.value,
                  nom: option.text
                };
                localStorage.setItem('Module', JSON.stringify(item));
              });
        }
        if (valeurLabel === "Salle" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            label.innerHTML = valeurLabel
            const select = document.createElement("select");
            select.id = "select"
            creationlisteDeroulantFormulaire(salles, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);

            select.addEventListener('change', function() {
                const option = select.options[select.selectedIndex];
                const item = {
                  id: option.value,
                  nom: option.text
                };
                localStorage.setItem('Salle', JSON.stringify(item));
              });
        }
        if (valeurLabel === "Classe" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            label.innerHTML = valeurLabel
            const select = document.createElement("select");
            select.id = "select"
            creationlisteDeroulantFormulaire(classes, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);

            select.addEventListener('change', function() {
                const option = select.options[select.selectedIndex];
                const item = {
                  id: option.value,
                  nom: option.text
                };
                localStorage.setItem('Classe', JSON.stringify(item));
              });
        }
        if (valeurLabel === "HeureDebut" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            label.innerHTML = valeurLabel
            const select = document.createElement("select");
            select.id = "select"
            creationlisteDeroulantFormulaire(HeureDebuts, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);

            select.addEventListener('change', function() {
                const option = select.options[select.selectedIndex];
                const item = {
                  id: option.value,
                  nom: option.text
                };
                localStorage.setItem('HeureDebut', JSON.stringify(item));
              });
        }
        if (valeurLabel === "HeureFin" &&  valeurLabel !=identification){
            const label = document.createElement("label");
            label.id= "label"
            label.innerHTML = valeurLabel
            const select = document.createElement("select");
            select.id = "select"
            creationlisteDeroulantFormulaire(HeureDebuts, select)
            coteLabel.appendChild(label)
            coteSelect.appendChild(select);

            select.addEventListener('change', function() {
                const option = select.options[select.selectedIndex];
                const item = {
                  id: option.value,
                  nom: option.text
                };
                localStorage.setItem('HeureFin', JSON.stringify(item));
              });
        }
        if (enseignants.find(nomEnseign => nomEnseign.id === valeur)){
            const nomEnseign = enseignants.find(nomEnseign => nomEnseign.id === valeur).nom ;
            const idEnseign = enseignants.find(nomEnseign => nomEnseign.id === valeur).id ;
           
            const item = {id: idEnseign, nom: nomEnseign};
            console.log(item);
            localStorage.setItem('Enseign', JSON.stringify(item));
        }
        
        localStorage.setItem('Jour', JSON.stringify(indice));

    })
}

function creationlisteDeroulantFormulaire(tableau, select) {
    select.innerHTML = "";
    tableau.forEach(eltTableau => {
            let option = document.createElement("option");
            option.setAttribute("value",eltTableau.id)
            option.text = eltTableau.nom;
            select.appendChild(option);
    });
}

function afficherFormulaire(identification, valeur){
    for ( i = 0; i < tabBoutonPlusDansJour.length; i++) {
        tabBoutonPlusDansJour[i].addEventListener("click", ()=>{
            coteLabel.innerHTML = ""
            coteSelect.innerHTML = ""
            zoneformulaire.style.display = "block"
            // if ( tabBoutonPlusDansJour[i].value
            console.log(tabBoutonPlusDansJour[i].getAttribute("value"))
            let  indice = i ;
            indice = indice.toString();

            formulaire(identification, indice, valeur)
           
        })
        
    }

 }
 const planningCours = []
listeDeroulant.addEventListener("change", (event) => {
    const valeur = event.target.value
    lundi.innerHTML = ""
    mardi.innerHTML = ""
    mercredi.innerHTML = ""
    jeudi.innerHTML = ""
    vendredi.innerHTML = ""
    samedi.innerHTML = ""
    coteLabel.innerHTML = ""
    coteSelect.innerHTML = ""
    zoneformulaire.style.display = "none"; 
    planning(valeur, cours)
  
    if (enseignants.find(monobjet => monobjet.id === valeur)){
        const nomValeur = enseignants.find(monobjet => monobjet.id === valeur).nom
        document.getElementById("nomPlaning").textContent = "Planning : "+ nomValeur
        const identification = "Enseignant"
        afficherFormulaire(identification, valeur)
      
            
    }
    if (classes.find(monobjet => monobjet.id === valeur)){
        const identification = "Classe"
        const nomValeur = classes.find(monobjet => monobjet.id === valeur).nom
        document.getElementById("nomPlaning").textContent = "Planning : "+ nomValeur
        afficherFormulaire(identification, valeur)
    }
    if (modules.find(monobjet => monobjet.id === valeur)){
        const identification = "Module"
        afficherFormulaire(identification, valeur)
    }
    if (salles.find(monobjet => monobjet.id === valeur)){
        const identification = "Salle"
        afficherFormulaire(identification, valeur)
    }

    ajouter.addEventListener("click", () =>{  
        zoneformulaire.style.display = "none";  
    
        coteLabel.innerHTML = ""
        coteSelect.innerHTML = ""  
        let enseignant = JSON.parse(localStorage.getItem('Enseign'));
        let module = JSON.parse(localStorage.getItem('Module'));
        let salle = JSON.parse(localStorage.getItem('Salle'));
        let classe = JSON.parse(localStorage.getItem('Classe'));
        let heureDebut = JSON.parse(localStorage.getItem('HeureDebut'));
        let heureFin = JSON.parse(localStorage.getItem('HeureFin'));
        let indice = JSON.parse(localStorage.getItem('Jour'));
        let cour = {
                    Enseign: enseignant.id,
                    Module: module.id,
                    Salle: salle.id,
                    Classe: classe.id,
                    HeureDebut: heureDebut.nom,
                    HeureFin: heureFin.nom,
                    jour : indice};
        
        
        cours.push(cour);
        lundi.innerHTML = ""
        mardi.innerHTML = ""
        mercredi.innerHTML = ""
        jeudi.innerHTML = ""
        vendredi.innerHTML = ""
        samedi.innerHTML = ""
        cour = {}
        planning(valeur, cours)
          
    })   
})
