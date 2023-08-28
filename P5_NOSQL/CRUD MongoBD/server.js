const express=require("express")
const axios = require('axios');
const pool = require('./db1');
const port=5200
const app=express()
var ApiPostRouter=require('./post.router').router
var ApiGetRouter=require('./get.router').router
var ApiDeleteRouter=require('./delete.route').router
var ApiUpdRouter=require('./update.route').router

var bodyPraser=require('body-parser')
app.use(bodyPraser.urlencoded({extended:false}));

app.set('view engine', 'ejs');

app.use(express.json())
app.use(express.urlencoded())

app.use('/api/',ApiPostRouter)
app.use('/api/',ApiGetRouter)
app.use('/api/',ApiDeleteRouter)
app.use('/api/',ApiUpdRouter)
app.use(express.static('public'))

app.get('/inscription', (req, res) => {

    
    const message = 'Hello, world!';
    axios.get('http://localhost:5200/api/recupere')
    .then(function (response) {
        let results = response.data; // Supposons que la réponse de votre API renvoie un tableau de résultats de recherche
        
        // Filtrez les résultats en fonction du modèle et du prix
        console.log(results)

        // Rendu de la vue EJS "recherchevoiture" avec les résultats de recherche
        res.render('./inscription', { results: results });
    })
    .catch(function (error) {
        console.error(error);
        res.status(500).send('Erreur lors de la recherche de voiture');
        res.render('./inscription', { message });
    });
    
   
});

app.listen(port,()=> console.log("le server a demarer au port " + port))