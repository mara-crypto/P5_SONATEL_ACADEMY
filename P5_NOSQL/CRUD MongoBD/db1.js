const MongoClient=require("mongodb").MongoClient

const url="mongodb://localhost:27017"

const dbName="newbase"

const connectToMongoDB = async () => {
    const client = new MongoClient(url, { useUnifiedTopology: true });
  
    try {
      await client.connect();
      console.log('Connecté à la base de données MongoDB');
      return client.db(dbName);
    } catch (error) {
      console.error('Erreur lors de la connexion à la base de données :', error);
      throw error;
    }
  };
  
  module.exports = connectToMongoDB;
  
  