

#Fonction pour recuperer la taille 
def mylen(liste):
    total=0
    for element in liste :

        total+=1
    return total


#fonction pour ajouter une element sur une liste
def myappend(liste,b):
    liste=liste +[b]
    return liste



#Fonction pour verifier la validiter d'un numero
def valide_numero(telephone) :
    telephone = str(telephone)
    if mylen(telephone)==9  and telephone[0]=="7" and telephone[1] in  ["8","7","6","5","0"]  :
        return True
    else:
        return False


#Fonction mysplit pour separer
def mysplit(text, separateur):
    textseparer = []
    current_part = ""
    for char in text:
        if char == separateur:
            textseparer=myappend(textseparer,current_part)
            current_part = ""
        else:
            current_part += char
    textseparer=myappend(textseparer,current_part)
    return textseparer




#Fonction Pour verifier la validiter d'une notes qui doit etre comprise entre 0 et 20 et etre un decimale avec 2 chiffre apres la virgule
def valide_note(note):

        note = (note)
        #entier, decimale = mysplit(note,";") 
        # entier = int(entier)
        # decimale = int(decimale)

        if (note >= '0') and (note <= '20') : #and (decimale >= 0) and (decimale<=99)  :
            return True
        else:
            return False
    

#Fonction pour Calculer moyenne 
def calcule_moy(note_devoir,note_projet,note_exam):
    note_devoir = float (note_devoir)
    note_exam = float (note_exam)
    note_projet = float (note_projet)
    moy = (note_devoir + note_projet + note_exam ) / 3
    
    return moy


#Fonction pour affichage du menu
def afficher_menu ():
    
    print("1- Afficher tout les informations de chaque etudiant ")
    print("2- Trier et afficher par ordre décroissant de la moyenne ")
    print("3- Rechercher selon le téléphone ")
    print("4- Modification de notes pour un étudiant ")
    print("5- Sortir ")
    choice = input("entrer votre choix ")
    return choice


#Fonction pour afficher les informations de toute les etudiants
def afficher_info(etudiants):

    print(100*'-')
    print("|{0:<12} |{1:<12}|{2:<12}|{3:<12}|{4:<12}|{5:<12}|{6:<12}|{7:<12}".format("Prénom","Nom","Classe","Téléphone","Devoir","Projet","Examen","Moyenne"))
    print(100*'-')

    for etudiant in etudiants:
        prenom, nom, classe, tel, dev, proj, exam, moy = etudiant
        print("|{0:<12} |{1:<12}|{2:<12}|{3:<12}|{4:<12.2f}|{5:<12.2f}|{6:<12.2f}|{7:<12.2f}".format(
            etudiant['Prenom'], etudiant['Nom'], etudiant['Classe'], etudiant['Telephone'],etudiant['Devoir'],etudiant['Projet'],etudiant['Exam'], etudiant['Moyenne']))

    print(100*'-')


#Fonction pour Trier et afficher (par ordre décroissant de la moyenne)
def trie_afficher(etudiants) :
    for i in range(mylen(etudiants) - 1):
        for j in range(i + 1, len (etudiants)) : 
            if etudiants[i]['Moy'] < etudiants[j]["Moy"] :
                etudiants [i], etudiants [j] = etudiants[j], etudiants[i]
    return etudiants


#Fonction Pour rechercher 
def rechercher(critere, valeur, etudiants):
    
    resultats = []
    if critere == "Telephone" :
        for etudiant in etudiants:
            if etudiant["Telephone"] == valeur:
                resultats = myappend(resultats, etudiant)
    elif critere == "Prenom":
        for etudiant in etudiants:
            if etudiant["Prenom"] == valeur:
                resultats = myappend(resultats, etudiant)
    elif critere == "Nom":
        for etudiant in etudiants:
            if etudiant["Nom"] == valeur:
                resultats = myappend(resultats, etudiant)
    elif critere == "Classe":
        for etudiant in etudiants:
            if etudiant["Classe"] == valeur:
                resultats = myappend(resultats, etudiant)
    else:
        print("Critère de recherche non valide.")
    
        return

    if resultats:
        afficher_info(resultats)
    else:
        print("Aucun résultat trouvé.")


#Fonction pour modifier les information d'un etudiant en donnant son numero de telephone
def modifier_info(tel,etudiants) :
    tel_in_etudiant = False
    for etudiant in etudiants:
        if etudiant["Telephone"] == tel :
            etudiant
            tel_in_etudiant = True
            break
    if tel_in_etudiant == True :
        choix=input("voulez vous modifier la note du devoir: o/n")
        if choix == "o" :
            devoir=input("donner la nouvelle note du devoir")
            etudiant["Devoir"] = devoir
        choix = input("voulez vous modifier la note du projet: o/n")
        if choix == "o" :
            projet=input("donner la nouvelle note pour le projet")
            etudiant["Projet"] = projet
        choix = input("voulez vous modifier la note de l'exam: o/n")
        if choix == "o" :
            exam=input("donner la nouvelle note pour l'exam")
            etudiant["Exam"] = exam

        etudiant["Devoir"] = float(etudiant["Devoir"])
        etudiant["Projet"] = float(etudiant["Projet"])
        etudiant["Exam"] = float(etudiant["Exam"])

        newmoy=calcule_moy(etudiant["Devoir"],etudiant["Projet"], etudiant["Exam"])
        etudiant["Moyenne"] = newmoy
        print("Les notes ont été modifiées avec succès.")
    else:
        print("le numero de tel n'appartient a aucun etudiant enregistre")


#Créer une fonction exit_program qui termine simplement l'exécution du programme.
def sortie_programme():
    print("Au revoir!")
    raise SystemExit











###########################################################################################################################################
                                                    #Fonction utiliser dans l'exercice 9

# Liste d'opérateurs téléphoniques valides
operateurs = ["Orange", "Tigo", "Expresso", "Promobile"]

# Saisie de l'opérateur téléphonique du client
def entre_operateur():
    while True:
        operateur = input("Entrez l'opérateur téléphonique du client (Orange, Tigo, Expresso, Promobile) : ")
        if operateur in operateurs:
            return operateur
        else:
            print("Opérateur téléphonique non valide. Veuillez réessayer.")



# Saisie des informations d'un client
def entrer_info_client():
    while True:
        nom = input("Entrez le préprenom du client : ")
        prenom = input("Entrez le prenom de famille du client : ")
        telephone = input("Entrez le numéro de téléphone du client : ")
        if nom and prenom and telephone:
            info_client = {"nom":nom, "prenom": prenom, "telephone": telephone}
            return info_client
        else:
            print("Toutes les informations du client sont obligatoires. Veuillez réessayer.")




# Matrice pour stocker les informations des clients
matrice_client = {}  
matrice_client= {"Orange":[{"nom":"diop", "prenom":"mara", "telephone":"783719445"}, {"nom":"ndiaye", "prenom":"mo", "telephone":"773719445"}],"Tigo":[{"nom":"dieng", "prenom":"demba", "telephone":"763719445"}, {"nom":"fall", "prenom":"moussa", "telephone":"762019440"}], "expresso":[{"nom":"diop", "prenom":"mara", "telephone":"703719445"}, {"nom":"ndiaye", "prenom":"mo", "telephone":"703710045"}], "Promobile":[{"nom":"mbengue", "prenom":"laye", "telephone":"751119645"}, {"nom":"seck", "prenom":"elhaj", "telephone":"753719445"}]}

# Ajout des informations d'un client à la matrice
def ajout_client_dans_matrice(operateur, info_client):
    if operateur not in matrice_client:
        matrice_client[operateur] = []
    matrice_client[operateur] = myappend(matrice_client[operateur], info_client)

# Affichage des informations de tous les clients dans la matrice
def afficher_client():
    for operateur, client in matrice_client.items():
        print("Clients de l'opérateur", operateur)
        for client in client:
            print("-", client["nom"], client["prenom"], ":", client["telephone"])



# Affichage des informations des clients pour un opérateur spécifique
def aficher_clients_par_operateur(operateur):
    if operateur in matrice_client:
        clients = matrice_client[operateur]
        print("Clients de l'opérateur", operateur)
        for client in clients:
            print("-", client["nom"], client["prenom"], ":", client["prenom"])
    else:
        print("Aucun client n'a été trouvé pour l'opérateur", operateur)



def modifier_ajouter_client_telephone(matrice_client):
    operateur_accepter = ["Orange", "Tigo", "Expresso", "Promobile"]
    operateur = input("donner le nom de l'operateur")
    if operateur not in operateur_accepter:
        print("Erreur: operateur n'est pas reconnue. Enter Orange, Tigo, Expresso ou Promobile.")
        return

    prenom = input("Entrer le prenom du client: ")
    nom = input("donner le nom du client")
    trouver = False
    for i in range(len(matrice_client[operateur])):
        client = matrice_client[operateur][i]
        if client["nom"] == nom and client["prenom"] == prenom :
            trouver = True
            break
    
    if trouver:
        nouveau_telephone = input("Enter un nouveau numero: ")
        matrice_client[operateur][i]["telephone"] = nouveau_telephone
        print("Numéro de téléphone modifier avec succès")
    else :
        numero_telephone = input("Entrer numero de telephone: ")
        client = {"name": nom, "prenom": prenom, "telephone": numero_telephone}
        matrice_client[operateur] = myappend(matrice_client[operateur], client)
        print("client ajoutée avec succes")



#Créer une fonction exit_program qui termine simplement l'exécution du programme.
def sortie_programme():
    print("Au revoir!")
    raise SystemExit

