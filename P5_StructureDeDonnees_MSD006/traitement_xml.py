import csv
import xml.etree.ElementTree as ET
import json
from traitement import *
from lxml import etree

def traiter_donnees_avec_xml() :

    # Ouvrir le fichier CSV en lecture
    with open('Donnees_Projet_Python_DataC5.csv', newline='') as csvfile:
        # Lire les données CSV en utilisant le module csv
        reader = csv.DictReader(csvfile)
        donne =[]

        for line in reader :
            donne.append(line)

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
                """ % (row["CODE"], row["Numero"], row["Nom"], row["Prénom"], transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(row["Date de naissance"]))), changer_format_classe(row["Classe"]), format_notes(row["Note"])  )
    

    with open('Donnees_Projet_Python_DataC5.xml',"w") as f :
        f.write("<?xml version='1.0' encoding='ISO-8859-1' standalone = 'no'  ?>\n <Eleves>")
        f.write("\n".join(convert_row(row) for row in donne))
        f.write("\n </Eleves>")

    
    eleve = {}
    dico = {}
    data = {}
    d = {}
    tree = etree.parse("Donnees_Projet_Python_DataC5.xml")
    for code,numero,nom,prenom,date,classe,note in tree.xpath("/Eleves/Eleve"):

        if  code.text == None :
            eleve["code"] = ""
        else :
            eleve["code"]= code.text

        if  numero.text == None :
            eleve["numero"] = ""
        else : 
            eleve["numero"] = numero.text

        if nom.text == None :
            eleve["nom"] = ""
        else :
            eleve["nom"]= nom.text

        if prenom.text == None :
            eleve["prenom"] = ""
        else :
            eleve["prenom"]= prenom.text

        if date.text == None :
            eleve["date"] = ""
        else :
            eleve["date"]= date.text

        if classe.text == None :
            eleve["classe"] = ""
        else :
            eleve["classe"]= classe.text

        if note.text == None :
            eleve["note"] = ""
        else :
            eleve["note"]= eval(str(note.text))

        data[numero.text] = eleve
        eleve = {}
  
    

    # print(data)

    (donnees_valides, donnees_invalides) = (separation_des_donnees_en_valide_et_invalide(data))
    # print(donnees_valides)

    format = input("dans quel format voulez vous mettre les donnee valide, CSV ou JSON ")
    while format != "CSV" and format != "JSON" :
        format = input("dans quel format voulez vous mettre les donnee valide, CSV ou JSON ")



    if format == "CSV" :

        with open('Donnees_Valides_csv.csv', 'w', ) as dv:
            [dv.write('{0}\n'.format(valeur)) for valeur in donnees_valides.values()]

        
        with open('Donnees_Invalides_json.json', 'w', encoding='utf-8') as dv:
            dv.write(json.dumps(donnees_invalides, indent=4))
        # donnees_invalides_json = json.dumps(donnees_invalides)
    


    else:  #format == "JSON" 
    
        with open('Donnees_Valides_json.json', 'w', encoding='utf-8') as dv:
            dv.write(json.dumps(donnees_invalides, indent=4))
        # donnees_invalides_json = json.dumps(donnees_valides)


        with open('Donnees_Invalides_csv.csv', 'w', ) as dv:
            [dv.write('{0}\n'.format(valeur)) for valeur in donnees_invalides.values()]

        



    


# traiter_donnees_avec_xml()