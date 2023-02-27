
tab = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Ocrobre', 'Novembre', 'Decembre', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]


booleen=True
while(booleen):
   print("1. Mois en Français")
   print("2. Mois en Anglais")
   print("3. Quitter")
   print('\n')
   entre = int(input("entrer un chiffre "))
   if entre==1 or entre==2 or entre==3 :
       booleen=False


booleenn=True       
while booleenn :
   if entre == 1 or entre==2 :
       if entre==1:
           debut=0
           fin= len(tab)//2
           d=3
       else :
           debut=len(tab)//2
           fin=len(tab)
           d =debut+3
       while debut<d :
           for i in range(debut,fin,3):
               print ( tab[i],end=(15-len(tab[i]))*' ')
           print('\n')
           debut = debut+1
   print("1. Mois en Français")
   print("2. Mois en Anglais")
   print("3. Quitter")
   print('\n')
   entre = int(input("entrer un chiffre "))
   if entre==3:
       booleenn=False
       exit()

