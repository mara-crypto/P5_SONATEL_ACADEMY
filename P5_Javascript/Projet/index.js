const listeDeroulant = document.getElementById("listeDeroulant") ;
const enseignantsDiv = document.getElementById("enseignant");
const sallesDiv = document.getElementById("salle");
const modulesDiv = document.getElementById("module");
const classesDiv = document.getElementById("classe");

const element1 = document.getElementById("element1");
const element2 = document.getElementById("element2");
const element3 = document.getElementById("element3");
const element4 = document.getElementById("element4");
const element5 = document.getElementById("element5");
const element6 = document.getElementById("element6");


const enseignants = [{nom: "Enseignants", id: "100", module:["300"]}, 
                     {nom: "Aly", id: "101", module:["305","306"]}, 
                     {nom: "Baila", id: "102", module:["305","306"]}, 
                     {nom: "Ndoye", id: "103", module:["305","306"]},
                     {nom: "Mbaye", id: "104", module:["302","303","301"]},
                     {nom: "Djiby", id: "105", module:["304"]}, 
                     {nom: "Seckouba", id: "106", module:["304","301"]}];

const classes = [{nom: "Classes", id: "200", nbrEleve: "00", salle:[00]}, 
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




const tabclassEnseiSalClassMod = document.querySelectorAll(".classEnseiSalClassMod ");
console.log(tabclassEnseiSalClassMod);
function m(){
    tabclassEnseiSalClassMod.forEach(elementTab => {
        elementTab.addEventListener("click", (event) => {
            const identifiant = (event.target.getAttribute("id"))
            console.log(identifiant)
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
            option.text = eltTableau.nom;
            listeDeroulant.appendChild(option);
    });
}

function recuperationNom(tableau){
    tableau.forEach(element => {
        const idelement = element.nom
        console.log(idelement)
    })
    
}
const cours = [
    {Enseign: "101",
    Module: "305",
    Salles: "206",
    Classe: "401",
    HeureDebut: "8h",
    HeureFin: "10",
    jour:"lundi" },

    {Enseign: "101",
    Module: "306",
    Salles: "",
    Classe: "",
    HeureDebut: "14h",
    HeureFin: "17h",
    jour: "lundi"},

    {Enseign: "101",
    Module: "",
    Salles: "",
    Classe: "",
    HeureDebut: "",
    HeureFin: "",
    jour: "mardi"},

    {Enseign: "101",
    Module: "",
    Salles: "",
    Classe: "",
    HeureDebut: "",
    HeureFin: "",
    jour: "mercredi"},

    {Enseign: "101",
    Module: "",
    Salles: "",
    Classe: "",
    HeureDebut: "",
    HeureFin: "",
    jour: "jeudi"}
]


listeDeroulant.addEventListener("change", (event) => {
    const valeur = event.target.value
    recuperationNom(enseignants)
        if (valeur === "Aly"){
            console.log("Aly est sélectionné");
            horaire2.innerHTML = ""
            element1.appendChild(horaire2)
        }
        if (valeur === "Mbaye"){
            console.log("Mbaye est sélectionné");
        }
});



let horaire2 = document.createElement("div")
horaire2.id = "horaire2";
horaire2.classList.add("horaire");

let horaire1 = document.createElement("div")
horaire1.id = "horaire1";
horaire1.classList.add("horaire");

let horaire3 = document.createElement("div")
horaire3.id = "horaire3";
horaire3.classList.add("horaire");

