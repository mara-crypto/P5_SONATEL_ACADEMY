
import validator from 'validator';
const email = 'test@gmail.com';

if (validator.isEmail(email)) {
    console.log('L\'adresse e-mail est valide.');
} else {
    console.log('L\'adresse e-mail est invalide.');
}

