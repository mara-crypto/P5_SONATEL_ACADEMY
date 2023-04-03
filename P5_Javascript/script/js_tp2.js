

const divGauche = document.createElement('div');
divGauche.id = 'divGauche';
const deuxDivBoutons = document.getElementById("deuxDivBoutons");
deuxDivBoutons.appendChild(divGauche);

const tableau = ["Mon Premier", "Mon Deuxieme", "Mon Troisieme", "Mon Quatrieme"];

for (let i = 0; i < tableau.length; i++) {
    const element = document.createElement("p");
    element.id = 'element-' + (i + 1);
    element.textContent = tableau[i];

    element.addEventListener("mouseover", () => {
        element.classList.add("selection");
    });

    element.addEventListener("mouseout", () => {
        element.classList.remove("selection");
    });

    element.addEventListener('click', function() {
        element.classList.toggle('selected');
        verifierBoutons();
    });

    divGauche.appendChild(element);
}


const boutons = document.createElement("div");
boutons.id = "boutons";
deuxDivBoutons.appendChild(boutons);


const divDroit = document.createElement('div');
divDroit.id = 'divDroit';
deuxDivBoutons.appendChild(divDroit);

const carreDroit = document.createElement('div');
carreDroit.classList.add("carre");



let boutonDroit = document.createElement('i');
boutonDroit.classList.add("bx", "bx-chevrons-right");
boutonDroit.style.color = 'black';
boutonDroit.style.fontSize = "30px";


carreDroit.appendChild(boutonDroit);
boutons.appendChild(carreDroit);

const carreGauche = document.createElement('div');
carreGauche.classList.add("carre");

let boutonGauche = document.createElement('i');
boutonGauche.classList.add('bx', 'bx-chevrons-left');
boutonGauche.style.disabled
boutonGauche.style.color = 'black';
boutonGauche.style.fontSize = "30px";


carreGauche.appendChild(boutonGauche);
boutons.appendChild(carreGauche);


function verifierBoutons() {
    if (divGauche.querySelector('.selected')) {
        boutonDroit.disabled = false;
    } else {
        boutonDroit.disabled = true;
    }
    if (divDroit.querySelector('.selected')) {
        boutonGauche.disabled = false;
    } else {
        boutonGauche.disabled = true;
    };
};

function deplacerDroite () {
    let element = divGauche.querySelector('.selected');
    if (element) {
        divDroit.appendChild(element);
        element.classList.remove('selected');
        verifierBoutons();
    };
};

function deplacerGauche() {
    let element = divDroit.querySelector('.selected');
    if (element) {
        divGauche.appendChild(element);
        element.classList.remove('selected');
        verifierBoutons();
    };
};

boutonDroit.addEventListener('click' , deplacerDroite);
boutonGauche.addEventListener('click', deplacerGauche);