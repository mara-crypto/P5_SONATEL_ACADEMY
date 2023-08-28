const express = require('express');


var ControUser=require('./controle')

exports.router=(function(){
  const router = express.Router();

  router.route('/recupere').get(ControUser.RecupereChambre);

  return router
})();
