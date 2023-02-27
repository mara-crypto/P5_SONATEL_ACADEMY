from traitement import *
import json
import csv

def traiter_donnees_avec_json() : 

    # Lire le fichier CSV et le convertir en JSON
    with open('Donnees_Projet_Python_DataC5.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)  # Ignorer la première ligne (en-tête)
        data = {}
        for row in csvreader:
            # key = row[1]
            # data[key] = row
            data[row[1]] = {
                'code': row[0],
                'numero': row[1],
                'nom': row[2],
                'prenom': row[3],
                'date_de_naissance': transformation_date(transformation_des_separateurs_en_tiret(espace_inutile(row[4]))),
                'classe': changer_format_classe(row[5]),
                'note': format_notes(row[6])
            }


    # Écrire les données dans un fichier JSON
    with open('Donnees_Projet_Python_DataC5.json', 'w', encoding='utf-8') as fichierjson:
        fichierjson.write(json.dumps(data, indent=4))


    with open("Donnees_Projet_Python_DataC5.json", 'r') as fichier :
        dico = json.load(fichier)
 


        
    (donnees_valides, donnees_invalides) = (separation_des_donnees_en_valide_et_invalide(data))


    format = input("dans quel format voulez vous mettre les donnee valide, CSV ou XML ")
    while format != "CSV" and format != "XML" :
        format = input("dans quel format voulez vous mettre les donnee valide, CSV ou XML ")



    if format == "CSV" :

        with open('Donnees_Valides_csv.csv', 'w', ) as dv:
            [dv.write('{0}\n'.format(valeur)) for valeur in donnees_valides.values()]
            
            # donnee = csv.writer(dv)donne_projet_xml
            # for valeur in donnees_valides.values() :
            #     for key,value in valeur.items() :
            #         donnee.writerow([value])
            #         donnee.writerow(",",end='')
        
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


        with open('Donnees_Invalides_csv.csv', 'w', ) as dv:
            [dv.write('{0}\n'.format(valeur)) for valeur in donnees_invalides.values()]




# traiter_donnees_avec_json()