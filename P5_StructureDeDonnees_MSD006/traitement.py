import re

def is_valid_numero(numero):
    regex = r'^[A-Z0-9]{7}$'
    if re.match(regex, numero):
        return True
    else:
        return False


def est_prenom_valide(prenom):

    if prenom == "":  # Si le prénom est vide, on le considère comme invalide
        return False
    else:
        if 'A' <= prenom[0] <= 'Z' and len(prenom) >= 3:  # Si la première lettre est une majuscule et que la longueur est d'au moins 3 caractères
            return True  # Le prénom est valide
        else:
            return False  # Le prénom n'est pas valide


def est_nom_valide(nom):

    if nom == "":
        # Si le nom est vide, il n'est pas valide
        return False
    else:
        # Vérifier que la première lettre est une majuscule et que la longueur du nom est supérieure ou égale à 2
        if 'A' <= nom[0] <= 'Z' and len(nom) >= 2:
            return True
        else:
            return False


def espace_inutile(date):

    if date == "" :
        return date
    else :
    # Supprime tous les espaces inutiles dans la date
    #date = date.replace(" ", "")
        date1 = ""
        if date[0] != " " :
            date1 = date1 + date[0]
        for i in range(1,len(date)) :
            if date[i-1] == " " and date [i] == " " :
                continue
            else :
                date1 = date1 + date[i] 
        return date1



def transformation_des_separateurs_en_tiret(date):

    date1 = ""
    # Parcourt chaque caractère de la date et remplace les séparateurs par des tirets
    for i in range(len(date)):
        if date[i] in [',', ';', ':', ' ', '/', '.', '_']:
            date1 += '-'
        else:
            date1 += date[i]
    return date1


import locale
from datetime import datetime

def transformation_date(date_string):

    # Configure la localisation en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
    try:
        # Tente de transformer la date en utilisant le format "%d-%B-%y"
        date_obj = datetime.strptime(date_string, "%d-%B-%y")
    except ValueError:
        try:
            # Si cela échoue, tente de transformer la date en utilisant le format "%d-%m-%y"
            date_obj = datetime.strptime(date_string, "%d-%m-%y")
        except ValueError:
            return date_string
    # Formate la date pour qu'elle soit au format "jj-mm-aaaa"
    formatted_date = datetime.strftime(date_obj, "%d-%m-%Y")
    return formatted_date


def est_bissextile(annee):

    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def date_de_naissance_valide(date):
    # Vérification de la présence de la date
    if date == "" or not (date[6:].isdigit())   :
        return False
    else:

        if date[3:5] in ['01', '03', '05', '07', '08', '10', '12']:
            if '01'<= date[:2] <= '31':
                return True
            else:
                return False
        elif date[3:5] in ['04', '06', '09', '11']:
            if '01'<= date[:2] <= '30':
                return True
            else:
                return False
        elif date[3:5] == '02':
            # Vérification de l'année bissextile
            if est_bissextile(int(date[6:])):
                if '01' <= date[:2] <= '29':
                    return True
                else:
                    return False
            else:
                if '01' <= date[:2] <= '28':
                    return True
                else:
                    return False


def changer_format_classe(classe):
    # initialisation de la variable format_classe
    format_classe = ""
    # parcourir chaque caractère de la chaine classe
    for i in range(len(classe)):
        # Si le caractère est compris entre '3' et '6' ou entre 'A' et 'B', l'ajouter au format de classe
        if '3' <= classe[i] <= '6' or 'A' <= classe[i] <= 'B':
            format_classe += classe[i]
    # renvoyer le nouveau format de la classe
    return format_classe


def is_valid_classe(classe):
    if len(classe) != 2:
        return False
    if not classe[0].isdigit():
        return False
    if classe[1] not in ['A', 'B']:
        return False
    if int(classe[0]) < 3 or int(classe[0]) > 6:
        return False
    return True


def format_notes(notes):
    # Vérifier si la chaine de notes est vide
    if notes == '':
        return notes
    else:
         # Initialiser une liste de notes et un dictionnaire de matières
       
        matiere_dic = {}
         # Supprimer les espaces et les guillemets
        notes = notes.replace("Science_Physique","PC")
        notes = notes.replace("Pc","PC")
        notes = notes.replace("pc","PC")

        notes = notes.replace("MATH", "Math")

        notes = notes.replace("ANGLAIS","Anglais")

        notes = notes.replace("FRANCAIS","Francais")
        notes = notes.replace("Français","Francais")

        notes = notes.replace(" ", '')
        notes = notes.replace('"', '')
         # Diviser les notes en fonction des matières
        notes = notes.split('#')
           # Supprimer les éléments vides de la liste des notes
        for i in notes:
            if i == '':
                notes.remove(i)
        # Traiter chaque matière et ses notes
        for i in range(len(notes)):
            # Initialiser une chaine de caractères pour stocker les notes
            note_dic = ""
             # Diviser les informations de la matière en fonction de la note
            for j in notes[i].split('['):
                # Ajouter la matière au dictionnaire et initialiser une liste de notes pour cette matière
                matiere_dic[j] = []
                  # Ajouter chaque note dans la liste de notes pour cette matière
                for k in notes[i].split('[')[1]:
                     # Vérifier si le caractère est un chiffre, une virgule ou un point
                    if k.isnumeric() or k == ',' or k == '.':
                        note_dic += k.replace(',', '.')
                    else:
                          # Ajouter la note à la liste de notes pour cette matière
                        matiere_dic[j].append(note_dic)
                        note_dic = ""
                break
         # Traiter chaque matière et calculer la moyenne
        for matiere, notes in matiere_dic.items():
            if len(notes) > 0:
                if len(notes) == 5:
                    if notes[0] and notes[1] and notes[2] and notes[3]:
                         # Calculer la moyenne des devoirs
                        moyenne_devoir = (float(notes[0]) + float(notes[1]) + float(notes[2]) + float(notes[3])) / 4
                        # Calculer la moyenne de la matière en fonction des coefficients des devoirs et du contrôle continu
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[4]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                     # Ajouter la moyenne de la matière à la liste de notes pour cette matière
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 4:
                    if notes[0] and notes[1] and notes[2]:
                        moyenne_devoir = (float(notes[0]) + float(notes[1]) + float(notes[2])) / 3
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[3]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 3:
                    if notes[0] and notes[1]:
                        moyenne_devoir = (float(notes[0]) + float(notes[1])) / 2
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[2]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else:
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                    matiere_dic[matiere].append(moyenne_matiere)
                elif len(notes) == 2:
                    if notes[0]:
                        moyenne_devoir = float(notes[0])
                        moyenne_matiere = round((moyenne_devoir + (2 * float(notes[1]))) / 3, 2)
                        moyenne_matiere = str(moyenne_matiere)
                    else: 
                        moyenne_matiere = 0.0
                        moyenne_matiere = str(moyenne_matiere)
                        moyenne_matiere = str(moyenne_matiere)

                    matiere_dic[matiere].append
                   
        return matiere_dic


def validiter_notes(matiere_dic) :

    if matiere_dic == "" :
        return False
    else :
        matiere_valide = 0
        for cle, valeur in matiere_dic.items() :
            
            compteur_note_valide = 0

            if len(valeur) == 0 :
                continue

           
            for i in range(len(valeur)) : 
                

                if isinstance(valeur[i], str) and valeur[i].strip() and 0 <= float(valeur[i]) <= 20:
                #if 0 <=float(valeur[i]) <= 20 :
                    compteur_note_valide += 1
                    #
                    
                else :
                    continue
            

            if compteur_note_valide == len(valeur) :
               
                matiere_valide = matiere_valide + 1

        
        if matiere_valide == len(matiere_dic) :
            return True
        else :
            return False
    
        

######################################################################################################################################################################################
##################################################################################################################################################################################

# import csv 

      

# filename = open('Donnees_Projet_Python_DataC5.csv')
# lignecompte = 0

# f = csv.reader(filename)
# dico = {}
# for ligne in  f :
#     if lignecompte >= 1 :
#         dico[ligne[1]] ={'code':ligne[0], 'numero':ligne[1], 'nom':ligne[2], 'prenom':ligne[3], 'date_de_naissance':transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(ligne[4]))), 'classe':changer_format_classe(ligne[5]), 'note': format_notes(ligne[6])       } 
#     lignecompte += 1

def separation_des_donnees_en_valide_et_invalide(dico) :

    dico_invalides = {}


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
            
    return dico_valides,dico_invalides









def menu():
    print("{:^25}".format("Menu:"))
    print("╔═════════╦═══════════════╗")
    print("║{:^9}║{:^15}║".format("Choix", "Format"))
    print("╠═════════╬═══════════════╣")
    print("║{:^9}║{:^15}║".format("1", "CSV"))
    print("║{:^9}║{:^15}║".format("2", "JSON"))
    print("║{:^9}║{:^15}║".format("3", "XML"))
    print("║{:^9}║{:^15}║".format("4", "Quitter"))
    print("╚═════════╩═══════════════╝")

    choice = input("entre votre choix: ")

