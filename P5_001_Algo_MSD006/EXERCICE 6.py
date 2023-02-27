        #Recuperation de l'ordre
ordre = int(input("Saisissez l'ordre de la matrice carrée : "))
while ordre < 4:
    print("L'ordre de la matrice doit être supérieur à 4.")
    ordre = int(input("Saisissez l'ordre de la matrice carrée : "))

        #Recuperation de la position
position=[]
positionpossible =['ADDP', 'EDDP', 'SDP', 'ADDS', 'EDDS', 'SDS']
while position not  in positionpossible :
   position=(input("Les choix pour la position de la couleur sont l : ADDP, EDDP, SDP, ADDS, EDDS, SDS  "))

        #Recuperation de la couleur
couleur=[]
couleurpossible=['rouge', 'vert','jaune', 'bleu', 'pink']
while couleur not in couleurpossible :
    couleur=input("vous devez choisir parmis les couleurs suivantes : rouge, vert, bleu, pink  ")

        #Declaration des variable qui recupere l
b='\033[0;34m' + 'B' + '\033[0m' 
r='\033[0;31m' + 'R' + '\033[0m'
v='\033[0;32m' + 'V' + '\033[0m'
j='\033[0;33m' + 'J' + '\033[0m'
p='\033[0;35m' + 'P' + '\033[0m'

if couleur == 'bleu':
    dessin = b
if couleur == 'rouge':
    dessin = r
if couleur == 'vert':
    dessin = v
if couleur == 'pink':
    dessin = p

        #Ecriture de la matrice selon la position et la couleur choisie
matrice = []
for i in range(ordre):
    ligne = []
    for j in range(ordre) :

        # si on est au dessus de la diagonnale principale
        if i < j and position == 'ADDP':
            ligne.append(dessin)
          
        #si on est en dessous de la diagonnale principale   
        elif i > j and position == "EDDP":
            ligne.append(dessin)

        #si on est sur la diagonnale principale
        elif i==j and position == "SDP" :
            ligne.append(dessin)

        #si on est au dessus de la diagonnale secondaire
        elif position =="ADDS" and i+j<=ordre-2 :
            ligne.append(dessin)

        # si on en dessous de la diagonnale secondaire
        elif position=="EDDS" and i+j>ordre-1 :
           ligne.append(dessin)

        # sur la diagonnale secondaire      
        elif position=="SDS" and i+j==ordre-1 :
           ligne.append(dessin)
        
        else:
            ligne.append("0")
    matrice.append(ligne)

#Affichage de la matrice.
for ligne in matrice :
    for i in range(ordre):
        print(ligne[i],end=(7*' '))
    print('\n')
    print('\n')


