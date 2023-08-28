
var bcrypt=require('bcrypt')
const connectToMongoDB=require('./db1')



const EMAIL_regax=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

const decription_Password='Le premier caractère du mot de passe doit être une lettre, il doit contenir au moins 4 caractères et pas plus de 15 caractères et aucun caractère autre que des lettres, des chiffres et le trait de soulignement ne peut être utilisé';

const Passwor_Regex=/^[a-zA-Z]\w{3,14}/

module.exports = {
    inscrire: async function(req, res) {
      try {
        
        const hotel = req.body.hotel;
        const Prix = req.body.Prix;
        const localisation = req.body.localisation;
        const ville = req.body.ville;

        console.log(hotel,ville,Prix,localisation)
  
       
        const db = await connectToMongoDB('newbase');
  
     
        await db.collection('Chambre').insertOne({ hotel:hotel, ville:ville, Prix:Prix, localisation: localisation});
  
        console.log('Données insérées avec succès');
        res.redirect('/inscription');
      } catch (error) {
        console.error('Erreur lors de l\'inscription :', error);
        return res.status(500).json({ message: 'Erreur lors de l\'inscription' });
      }
    },

    UpdateChambre:async function(req, res) {
        try {

          const id = req.body.ide;
          const hotele = req.body.hotele;
          const Prixe = req.body.Prixe;
          const localisatione = req.body.localisatione;
          const villee = req.body.villee;
          console.log(id)
          const db = await connectToMongoDB('newbase');
          const data=await db.collection('Chambre').find({}).toArray();

          const hotel = data[id-1].hotel;
          const Prix = data[id-1].Prix;
          const localisation = data[id-1].localisation;
          const ville = data[id-1].ville;
          
         
    
         
          await db.collection('Chambre').updateOne(
            { hotel: hotel, ville: ville, Prix: Prix, localisation: localisation },
            { $set: { hotel:hotele,ville:villee,Prix:Prixe,localisation:localisatione } }
        );
          console.log('Données mise a jour avec succès');
          res.redirect('/inscription');
        } catch (error) {
          console.error('Erreur lors de l\'inscription :', error);
          return res.status(500).json({ message: 'Erreur lors du mise a jour' });
        }
      },

      RecupereChambre:async function(req, res) {
        try {
          
            
    
          
          const db = await connectToMongoDB('newbase');
    
       
          const data=await db.collection('Chambre').find({}).toArray();
    
          console.log('Données insérées avec succès');
         return res.status(200).json(data)
        } catch (error) {
          console.error('Erreur lors de l\'inscription :', error);
          return res.status(500).json({ message: 'Erreur lors de l\'inscription' });
        }
      },
      DeleteChambre:async function(req, res) {
        try {
            const id =req.body.id;
    
       
          const db = await connectToMongoDB('newbase');
          const data=await db.collection('Chambre').find({}).toArray();

          const hotel = data[id-1].hotel;
          const Prix = data[id-1].Prix;
          const localisation = data[id-1].localisation;
          const ville = data[id-1].ville;

          console.log(hotel,Prix,localisation,ville)

          await db.collection('Chambre').deleteOne({hotel:hotel,ville:ville,Prix:Prix,localisation:localisation});
    
          console.log('Données suprimé avec succès');
         
        } catch (error) {
          console.error('Erreur lors de l\'inscription :', error);
          return res.status(500).json({ message: 'Erreur lors de l\'inscription' });
        }
      },



  };
  

    // {% comment %} db.createUser({user:"mouhamed",pwd:"mou123",roles:[{role:"readWrite",db:"newbasse"},{role:"dbAdmin",db:"newbase"}]}); {% endcomment %}