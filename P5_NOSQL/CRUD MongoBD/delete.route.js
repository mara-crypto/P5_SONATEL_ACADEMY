const express = require('express');


var ControUser=require('./controle')

exports.router=(function(){
  const router = express.Router();

  router.route('/suprimer/:id').delete(ControUser.DeleteChambre);

  return router
})();