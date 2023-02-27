import csv
import json
import xml.etree.ElementTree as ET
from traitement import *

def traiter_donnees_avec_csv() :
    import csv 
    filename = open('Donnees_Projet_Python_DataC5.csv')
    lignecompte = 0
    f = csv.reader(filename)

    dico = {}


    for ligne in  f :
        if lignecompte >= 1 :
            dico[ligne[1]] ={'code':ligne[0], 'numero':ligne[1], 'nom':ligne[2], 'prenom':ligne[3], 'date_de_naissance':transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(ligne[4]))), 'classe':changer_format_classe(ligne[5]), 'note': format_notes(ligne[6])       } 
        lignecompte += 1

    (donnees_valides, donnees_invalides) = (separation_des_donnees_en_valide_et_invalide(dico))
    

    format = input("dans quel format voulez vous mettre les donnee valide, JSON ou XML ")
    while format != "JSON" and format != "XML" :
        format = input("dans quel format voulez vous mettre les donnee valide, JSON ou XML ")

    if format == "JSON" :

        with open('Donnees_Valides_json.json', 'w', encoding='utf-8') as dv:
            dv.write(json.dumps(donnees_valides, indent=4))
        # donnees_valides_json = json.dumps(donnees_valides)



        def convert_row(row) :
                return """
            <Eleve>
                <Code>%s</Code>
                <Numero>%s</Numero> 
                <Nom>%s</Nom>
                <Prenom>%s</Prenom>
                <Date_de_naissance>%s</Date_de_naissance>
                <Classe>%s</Classe>
                <Notes>%s</Notes>
            </Eleve>
                        """ % (row["code"], row["numero"], row["nom"], row["prenom"], row["date_de_naissance"], row["classe"], row["note"]  )
        
        with open('Donnees_Invalides_xml.xml',"w") as f :
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone = 'no'  ?>\n <Eleves>")
            f.write("\n".join(convert_row(valeur) for cle, valeur in donnees_invalides.items()))
            f.write("\n </Eleves>")

        
            

    else :

        def convert_row(row) :
                return """
            <Eleve>
                <Code>%s</Code>
                <Numero>%s</Numero> 
                <Nom>%s</Nom>
                <Prenom>%s</Prenom>
                <Date_de_naissance>%s</Date_de_naissance>
                <Classe>%s</Classe>
                <Notes>%s</Notes>
            </Eleve>
                        """ % (row["code"], row["numero"], row["nom"], row["prenom"], row["date_de_naissance"], row["classe"], row["note"]  )
        
        with open('Donnees_Valides_xml.xml',"w") as f :
            f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone = 'no'  ?>\n <Eleves>")
            f.write("\n".join(convert_row(valeur) for cle, valeur in donnees_valides.items()))
            f.write("\n </Eleves>")

        
        with open('Donnees_Invalides_json.json', 'w', encoding='utf-8') as dv:
            dv.write(json.dumps(donnees_invalides, indent=4))
        # donnees_invalides_json = json.dumps(donnees_invalides)


 


# traiter_donnees_avec_csv()
