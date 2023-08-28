const express = require('express');


var ControUser=require('./controle')

exports.router=(function(){
  const router = express.Router();

  router.route('/inscription').post(ControUser.inscrire);

  return router
})();
