# from Fonction import mylen
# from Fonction import valide_note
# from Fonction import valide_numero
# from Fonction import myappend
# from Fonction import calcule_moy
# from Fonction import afficher_menu
# from Fonction import afficher_info
from Mes_fonctions import *

#Mon example
#etudiants=[{'Nom':'Diop','Prenom':'Modou','Telephone':'783719445','Classe':'Dev','Devoir':12,'Projet':13,'Exam':13,'Moyenne':12.5}]



etudiants=[]
continue_remplissage= True
while continue_remplissage :
    etudiant={}

        
    nom=input("Saisisser le nom ")
    etudiant['Nom']=nom

    prenom=input("Saisisser le prenom ")
    etudiant['Prenom']=prenom

    
    telephone=input("entrer le numero de telephone ")
    telephonecorrect=valide_numero(telephone)
    while telephonecorrect == False:
        telephone=input("entrer le numero de telephone ")
        telephonecorrect=valide_numero(telephone) 
    etudiant['Telephone']=telephone
          

    classe=input("Saisisser la classe ")
    etudiant['Classe']=classe

    devoircorrect=False
    while devoircorrect == False :
        devoir=input("saisisser la note du devoir ")
        if valide_note(devoir) == True :
            etudiant['Devoir']=devoir
            devoircorrect=True
        else :
            print("la note du devoir doit etre un decimale et comprise entre 0 et 20 ")
            
    projetcorrect=False
    while projetcorrect == False :
        projet=input("saisisser la note de projet ")
        if valide_note(projet) == True :
            etudiant['Projet']=projet
            projetcorrect=True
        else :
            print("la note de projet doit etre un decimale et comprise entre 0 et 20 ")

    examcorrect=False
    while examcorrect == False :
        exam=input("saisisser la note d'exam ")
        if valide_note(exam) == True :
            etudiant['Exam'] = exam 
            examcorrect = True
        else :
            print("la note d'exam doit etre un decimale et comprise entre 0 et 20 ")


    etudiant['Moyenne'] = (calcule_moy(devoir,projet,exam))

        
    etudiants = myappend(etudiants,etudiant)
    
    autrechoix = input("Souhaitez-vous entrer les informations d'un autre étudiant? (o/n)")
    if autrechoix == 'n':
      continue_remplissage = False
  


# afficher = afficher_menu()
choice=afficher_menu()

while choice != '5':
    if choice == '1' :
        print(afficher_info(etudiants))
        choice=afficher_menu()

    elif choice == '2' :
        print(afficher_info(trie_afficher(etudiants)))
        choice=afficher_menu()

    elif choice == '3' :
        critere = input("Veuillez entrer le critère de recherche (téléphone, nom, prénom ou classe): ")
        valeur = input("Veuillez entrer la valeur de recherche: ")
    
        if critere == "Telephone" :
            if valide_numero(valeur) == True:
                print("le numero de telephone est correct ")
            else:
                valeurcorrect=False
                while valeurcorrect == False:
                    valeur = input("Veuillez entrer la valeur de recherche: ")
                    if valide_numero(valeur) == True :
                        valeurcorrect = True
        print(rechercher(critere, valeur, etudiants))
        choice=afficher_menu()

    elif choice == '4' :
        tel=input("donner le numero de telephone de l'etudiant")
        print(modifier_info(tel, etudiants))
        choice=afficher_menu()

    else  :
        print("Choisis quelque chose")
        choice=afficher_menu()
   
    