library(stringr)
source("fonction.R")


Sys.setlocale("LC_TIME", "fr_FR.UTF-8")


donnecsv = read.csv("Donnees_Projet_Python_DataC5.csv", sep = ",",all=TRUE)

summary(donnecsv)

donne_valide = data.frame(
  Code = character(),
  Numero = numeric(),
  Nom = character(),
  Prenom = character(),
  Date.de.naissance = character(),
  Classe = character(),
  Note = character()
)

donne_invalide = data.frame(
  Code = character(),
  Numero = numeric(),
  Nom = character(),
  Prenom = character(),
  Date.de.naissance = character(),
  Classe = character(),
  Note = character()
)


separation = separation_des_donnees_en_valide_et_invalide(donnecsv)

donne_valide = rbind(donne_valide, separation[[1]] )
donne_valide
donne_invalide =  rbind(donne_invalide, separation[[2]] )
donne_invalide

