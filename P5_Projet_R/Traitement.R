donnecsv = read.csv("Donnees_Projet_Python_DataC5.csv", sep = ",",all=TRUE)

summary(donnecsv)

library(stringr)

a = donnecsv[,2]

str_length(a)

for (i in a) {
  print(i)
}
