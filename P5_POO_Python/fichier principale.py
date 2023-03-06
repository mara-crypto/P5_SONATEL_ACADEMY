import csv 
import locale
from datetime import datetime
import re


class Note:
    def __init__(self,note_c):
        self.note = note_c

    
    def format_notes(self, notes):
        if notes == '':
            return notes
        else:
            matiere_dic = {}
            notes = notes.replace("Science_Physique","PC")
            notes = notes.replace("Pc","PC")
            notes = notes.replace("pc","PC")
            notes = notes.replace("MATH", "Math")
            notes = notes.replace("ANGLAIS","Anglais")
            notes = notes.replace("FRANCAIS","Francais")
            notes = notes.replace("Français","Francais")
            notes = notes.replace(" ", '')
            notes = notes.replace('"', '')
            notes = notes.split('#')
            
            for i in notes:
                if i == '':
                    notes.remove(i)
            for i in range(len(notes)):
                note_dic = ""
                for j in notes[i].split('['):
                    matiere_dic[j] = []
                    for k in notes[i].split('[')[1]:
                        if k.isnumeric() or k == ',' or k == '.':
                            note_dic += k.replace(',', '.')
                        else:
                            matiere_dic[j].append(note_dic)
                            note_dic = ""
                    break
            for matiere, notes in matiere_dic.items():
                if len(notes) > 0:
                    if len(notes) == 5:
                        if notes[0] and notes[1] and notes[2] and notes[3]:
                            moyenne_devoir = (float(notes[0]) + float(notes[1]) + float(notes[2]) + float(notes[3])) / 4
                            moyenne_matiere = round((moyenne_devoir + (2 * float(notes[4]))) / 3, 2)
                            moyenne_matiere = str(moyenne_matiere)
                        else:
                            moyenne_matiere = 0.0
                            moyenne_matiere = str(moyenne_matiere)
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



class Etudiants :
    def __init__(self,code,numero,nom,prenom,date,classe,note):
        self.nom = nom
        self.prenom = prenom
        self.note = note
        self.numero = numero
        self.date = date
        self.code = code
        self.classe = classe
    
    def __str__(self) :
        return f"{self.code},{self.numero},{self.nom},{self.prenom},{self.date},{self.classe},{self.note}"


class Fichier:
    def __init__(self) :
        pass

    def lire_fichier(self,fichiercsv) :
        filename = open(fichiercsv)
        lignecompte = 0
        f = csv.reader(filename)

        dico = {}
        for ligne in  f :
            if lignecompte >= 1 :
                dico[ligne[1]] ={'code':ligne[0], 'numero':ligne[1], 'nom':ligne[2], 'prenom':ligne[3], 'date_de_naissance':ligne[4], 'classe':(ligne[5]), 'note': (ligne[6])       } 
            lignecompte += 1
        
        donne = {}
        for cle,valeur in dico.items() :
            Etudiant = Etudiants(valeur["code"],valeur["numero"],valeur["nom"],valeur["prenom"],valeur["date_de_naissance"],valeur["classe"],Note.format_notes(self,valeur["note"])) 
            etu = {"code":Etudiant.code, "numero":Etudiant.numero, "nom":Etudiant.nom, 'prenom':Etudiant.prenom, "date":Etudiant.date, "classe":Etudiant.classe, "note":Etudiant.note}
            donne[valeur["numero"]] = etu

        return donne
        

    def is_valid_numero(numero):
        regex = r'^[A-Z0-9]{7}$'
        if re.match(regex, numero):
            return True
        else:
            return False


    def est_prenom_valide(prenom):
        if prenom == "": 
            return False
        else:
            if 'A' <= prenom[0] <= 'Z' and len(prenom) >= 3:  
                return True 
            else:
                return False  


    def est_nom_valide(nom):
        if nom == "":
            return False
        else:
            if 'A' <= nom[0] <= 'Z' and len(nom) >= 2:
                return True
            else:
                return False


    def espace_inutile(date):
        if date == "" :
            return date
        else :
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
        for i in range(len(date)):
            if date[i] in [',', ';', ':', ' ', '/', '.', '_']:
                date1 += '-'
            else:
                date1 += date[i]
        return date1


    def transformation_date(date_string):
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        try:
            date_obj = datetime.strptime(date_string, "%d-%B-%y")
        except ValueError:
            try:
                date_obj = datetime.strptime(date_string, "%d-%m-%y")
            except ValueError:
                return date_string
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
                anne = Fichier.est_bissextile(int(date[6:]))
                                              
                if anne == True :
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
        format_classe = ""
        for i in range(len(classe)):
            if '3' <= classe[i] <= '6' or 'A' <= classe[i] <= 'B':
                format_classe += classe[i]
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
                        compteur_note_valide += 1
                    else :
                        continue
                if compteur_note_valide == len(valeur) :
                    matiere_valide = matiere_valide + 1
            if matiere_valide == len(matiere_dic) :
                return True
            else :
                return False



    def separation_des_donnees_en_valide_et_invalide(self,don) :
        dico_invalides = {}
        dico_valides = {}
        for cle, valeur in don.items() : 
            valeur_valide = 0
            if valeur["code"] != "" :
                valeur_valide += 1
            if Fichier.is_valid_numero(valeur["numero"]) == True :
                valeur_valide += 1
            if Fichier.est_nom_valide(valeur["nom"]) == True :
                valeur_valide += 1
            if Fichier.est_prenom_valide(valeur["prenom"]) == True :
                valeur_valide += 1
            if Fichier.date_de_naissance_valide(Fichier.transformation_date(Fichier.transformation_des_separateurs_en_tiret(Fichier.espace_inutile(valeur["date"])))) == True :
                valeur_valide += 1
            if Fichier.is_valid_classe(Fichier.changer_format_classe(valeur["classe"])) == True :
                valeur_valide += 1
            if Fichier.validiter_notes(valeur["note"]) == True :
                valeur_valide += 1

            if len(valeur) != valeur_valide :
                        dico_invalides[cle] = valeur
            else :
                        dico_valides[cle] = valeur 
        return dico_valides,dico_invalides
    


    def afficher_info(self) :
        donne = Fichier.lire_fichier(self, "Donnees_Projet_Python_DataC5.csv")
        for cle, valeur in donne.items() :
            print(valeur)


            
class principale :

    fichier = Fichier()
    m = fichier.lire_fichier('Donnees_Projet_Python_DataC5.csv')
    # fichier.afficher_info()
    donnees_valides,donnees_invalides = fichier.separation_des_donnees_en_valide_et_invalide(m)

