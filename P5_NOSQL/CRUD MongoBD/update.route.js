const express = require('express');


var ControUser=require('./controle')

exports.router=(function(){
  const router = express.Router();

  router.route('/update').post(ControUser.UpdateChambre);

  return router
})();