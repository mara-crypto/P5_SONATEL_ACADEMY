
ordre = int(input("Saisissez l'ordre de la matrice carrée : "))
while ordre <= 5:
   print("L'ordre de la matrice doit être supérieur à 5.")
   ordre = int(input("Saisissez l'ordre de la matrice carrée : "))


couleur = ""
while couleur not in ["Bleu", "Rouge"]:
   couleur = input("Choisissez une couleur (Bleu ou Rouge) : ")


position = ""
while position not in ["Haut", "Bas"]:
   position = input("Choisissez une position (Haut ou Bas) : ")

b='\033[0;34m' + 'B' + '\033[0m' 
r='\033[0;31m' + 'R' + '\033[0m'
matrice = []
for i in range(ordre):
   ligne = []
   for j in range(ordre):
        if i < j and position == "Haut":
            if couleur== "Bleu" :
                #ligne.append(couleur)
                ligne.append(b)
            else:
                ligne.append(r)
        elif i > j and position == "Bas":
            if couleur== "Bleu" :
                #ligne.append(couleur)
                ligne.append(b)
            elif couleur=="Rouge" :
                ligne.append(r)

        else:
           ligne.append("0")
   matrice.append(ligne)


for ligne in matrice :
    for i in range(ordre):
        print(ligne[i],end=(7*' '))
    print('\n')
    print('\n')




  


