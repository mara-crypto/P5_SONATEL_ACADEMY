

const serie1 = document.getElementById("serie1")
const serie2 = document.getElementById("serie2")
const serie3 = document.getElementById("serie3")
const serie4 = document.getElementById("serie4")
const serie5 = document.getElementById("serie5")
const serie6 = document.getElementById("serie6")

const resultat = document.getElementById("resultat")
const messageScore = document.getElementById("messageScore")
const rejouer = document.getElementById("rejouer")

const suivant1 = document.getElementById("suivant1")
const suivant2 = document.getElementById("suivant2")
const suivant3 = document.getElementById("suivant3")
const suivant4 = document.getElementById("suivant4")
const suivant5 = document.getElementById("suivant5")
const suivant6 = document.getElementById("suivant6")

const reponses1 = document.querySelectorAll('input[name="q1"]');
const reponses2 = document.querySelectorAll('input[name="q2"]');
const reponses3 = document.querySelectorAll('input[name="q3"]');
const reponses4 = document.querySelectorAll('input[name="q4"]');
const reponses5 = document.querySelectorAll('input[name="q5"]');
const reponses6 = document.querySelectorAll('input[name="q6"]');



function calculateScore() {
   let score = 0;
   
   reponses1.forEach(reponse => {
      console.log(reponse.checked)
       if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
       score++;
       }
   });
   reponses2.forEach(reponse => {
      console.log(reponse.checked)
       if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
       score++;
       }
   });
   reponses3.forEach(reponse => {
      console.log(reponse.checked)
       if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
       score++;
       }
   });
   reponses4.forEach(reponse => {
      console.log(reponse.checked)
       if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
       score++;
       }
   });
   reponses5.forEach(reponse => {
      console.log(reponse.checked)
      if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
      score++;
      }
  });   
  reponses6.forEach(reponse => {
   console.log(reponse.checked)
      if (reponse.checked && reponse.getAttribute('data-reponseCorrect') === "true") {
      score++;
      }
});
   return score;
}




function activerBouton (tableau, suivant){
   tableau.forEach(function(element) {
      let reponseSelected = false ;
      element.addEventListener("change", function() {
         if (this.checked){
            reponseSelected = true ;
         }
         if (reponseSelected) {
            suivant.disabled = false;
         } else {
            suivant.disabled = true ;
         }
      })
   })  
};

serie2.style.display = "none";
serie3.style.display = "none";
serie4.style.display = "none";
serie5.style.display = "none";
serie6.style.display = "none";
resultat.style.display = "none";

activerBouton(reponses1, suivant1);
suivant1.addEventListener('click', () =>{
   serie1.style.display = 'none';
   serie2.style.display = "block";
 })

activerBouton(reponses2, suivant2);
suivant2.addEventListener('click', () =>{
   serie2.style.display = 'none';
   serie3.style.display = "block";
})

activerBouton(reponses3, suivant3);
suivant3.addEventListener('click', () =>{
   serie3.style.display = 'none';
   serie4.style.display = "block";
})

activerBouton(reponses4, suivant4);
suivant4.addEventListener('click', () =>{
   serie4.style.display = 'none';
   serie5.style.display = "block";
})

activerBouton(reponses5, suivant5);
suivant5.addEventListener('click', () =>{
   serie5.style.display = 'none';
   serie6.style.display = "block";
})


activerBouton(reponses6, suivant6);
suivant6.addEventListener('click', () =>{
   const scorefinal = calculateScore();
   serie6.style.display = 'none';
   resultat.style.display = "block";
   messageScore.innerText = `Bravo ! Vous avez trouvé ${scorefinal}/6.`;
});


function desactiverBouton (tableau, suivant) {
   tableau.forEach(element => {
      element.checked = false ;
      suivant.disabled = true ;
   })
};

rejouer.addEventListener("click", ()=> {
   resultat.style.display = "none";
   serie1.style.display = "block";
   desactiverBouton(reponses1, suivant1);
   desactiverBouton(reponses2, suivant2);
   desactiverBouton(reponses3, suivant3);
   desactiverBouton(reponses4, suivant4);
   desactiverBouton(reponses5, suivant5);
   desactiverBouton(reponses6, suivant6);

});

