import './style.css'


import moment from 'moment';

function updateCountdown(date) {
  const targetDate = moment(date); // Date cible du compte à rebours
  const currentDate = moment(); // Date actuelle

  const diff = targetDate.diff(currentDate); // Différence entre les deux dates en millisecondes

  const duration = moment.duration(diff); // Convertit la différence en un objet de durée

  const days = Math.floor(duration.asDays()); // Nombre de jours complets dans la durée
  const hours = duration.hours();
  const minutes = duration.minutes();
  const seconds = duration.seconds();


  const countdownElement = document.getElementById('countdown');
  countdownElement.textContent = `Compte à rebours : ${days} jours, ${hours} heures, ${minutes} minutes, ${seconds} secondes`;
}

// Met à jour le compte à rebours toutes les secondes
setInterval(updateCountdown('2025-01-01'), 1000);

// Appel initial pour éviter un délai d'une seconde avant le premier affichage
updateCountdown('2025-01-01');
