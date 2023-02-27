
from projet import *


######################################################################################################################################################################################
##################################################################################################################################################################################

import csv 

      

filename = open('Donnees_Projet_Python_DataC5.csv')
lignecompte = 0

f = csv.reader(filename)
dico = {}

dico_invalides = {}

for ligne in  f :
    if lignecompte >= 1 :
        dico[ligne[1]] ={'code':ligne[0], 'numero':ligne[1], 'nom':ligne[2], 'prenom':ligne[3], 'date_de_naissance':transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(ligne[4]))), 'classe':changer_format_classe(ligne[5]), 'note': format_notes(ligne[6])       } 
    lignecompte += 1


dico_valides = {}
donne = {}

for cle, valeur in dico.items() : 
    valeur_valide = 0
    val = ""
    for key, value in valeur.items() :
        if key == 'code' :
            if value != "" :
                valeur_valide += 1
        
        elif key == "numero" :
            if is_valid_numero(value) == True :
               # print("test1")
                valeur_valide += 1
            
        elif key == "nom" :
            if est_nom_valide(value) == True :
                valeur_valide += 1
               # print("test2")
                
        elif key == "prenom" :
            if est_prenom_valide(value) == True :
                valeur_valide += 1
               # print("test6")
                
        elif key == "date_de_naissance" :
            if date_de_naissance_valide(value) == True :
                valeur_valide += 1
                #print("test3")
                
        elif key == "classe" :
            if is_valid_classe(value) == True :
                valeur_valide += 1
                #print("test4")
            
        elif key == "note" :
            if validiter_notes(value) == True :
                valeur_valide += 1
                #print("test5")
    #print("fin1")

         

    if len(valeur) != valeur_valide :
                dico_invalides[cle] = valeur
    else :
                dico_valides[cle] = valeur
        



choice = afficher_le_menu()

while choice != '9':
    if choice == '1' :
        print(afficher_information(dico_valides))
        choice = afficher_le_menu()


    elif choice == '2' :
        print(afficher_information(dico_invalides))
        choice = afficher_le_menu()
        
        
        
    elif choice == '3' :
        numero_de_recherche = input("Veuillez entrer le numero de l'eleve pour faire la recherche: ")
        if is_valid_numero(numero_de_recherche) == True :
            print("Le numero saisie est correct ")
        else :
            numero_est_correct = False
            while numero_est_correct == False:
                numero = input("Veuillez entrer un bon numero de recherche: ")
                if is_valid_numero(numero) == True :
                    valeurcorrect = True
        eleve_trouver = recherche_information(numero_de_recherche, dico_valides)
        if eleve_trouver == False :
            eleve_trouver = recherche_information(numero_de_recherche, dico_invalides)
            if eleve_trouver == False:
                print("Aucun élève trouvé pour le numéro de recherche donné.")
        choice = afficher_le_menu()



    elif choice == '4' :
        print(afficher_information(dico[0:5]))
        print(afficher_information(dico_valides[0:5]))
        print(afficher_information(dico_invalides[0:5]))
        choice = afficher_le_menu()
        
        
    elif choice == '5' :
        print(ajouter_information(dico))
        choix = input("voulez vous ajouter un autre eleves? (o/n) ")
        while choix == 'o' :
            print(ajouter_information(dico))
            choix = input("voulez vous ajouter un autre eleves? (o/n) ")
        choice = afficher_le_menu()
        
    
    elif choice == '6' :
        print
    
    
    elif choice == '7' :
        print
        
    
    elif choice == '9' :
        print
        

    else  :
        print("Choisis quelque chose")
        choice = afficher_le_menu()









