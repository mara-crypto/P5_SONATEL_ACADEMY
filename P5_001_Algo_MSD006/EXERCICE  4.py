
#chaine=input("Donner une chaine de plusieur chiffre separer par des tirets et mettez un tiret a la fin de la chaîne ")
chaine="78 371 55 56-76yzr ez263 78 90-257 8-762534111111-2134567890987654356-781234567-701234567"


numero_valide=[]
numero_invalide=[]
operateur={'78':0,'77':0,'76':0,'75':0,'70':0}
numero=""

numero=""

for i in range (len(chaine)):
   if (chaine[i]>='0' and chaine[i]<='9'):
       numero=numero+chaine[i]
   else:
       if chaine[i]=="-":
           # Vérifier que le numéro ne contient que des chiffres
           numero_validess = True
           for chiffre in numero:
               if not (chiffre>='0' and chiffre<='9'):
                   numero_validess = False
                   break
           if numero_validess and len(numero) == 9 and numero[0:2] in operateur.keys() :
               numero_valide.append(numero)
               operateur[numero[0:2]]+=1
           else :
               numero_invalide.append(numero)
           numero=""

# Ajoutez ce traitement pour traiter le dernier nombre
if numero != "":
    numero_validess = True
    for chiffre in numero:
        if not (chiffre >= '0' and chiffre <= '9'):
            numero_validess = False
            break
    if numero_validess and len(numero) == 9 and numero[0:2] in operateur.keys():
        numero_valide.append(numero)
        operateur[numero[0:2]] += 1
    else:
        numero_invalide.append(numero)



if len(numero_valide) >= len(numero_invalide) :
    taille_max = len(numero_valide)
else :
    taille_max = len(numero_invalide)




for i in range(taille_max) :
    if i < len(numero_valide):
        print(numero_valide[i],      )
    if i< len(numero_invalide):
        print(end=(70-len(numero_valide[i]))*' ')
        print(numero_invalide[i])
    print('\n')
for (cle , valeur) in operateur.items():
    if valeur != 0 :
        print("le nombre de numéro pour l'opérateur ",cle,"est :",valeur)