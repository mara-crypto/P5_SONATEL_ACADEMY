from traitement_csv  import traiter_donnees_avec_csv
from traitement_json import traiter_donnees_avec_json
from traitement_xml import traiter_donnees_avec_xml
from traitement import menu
from os import system


choice = menu()

while choice != '4' :

    if choice == '1' :
        print(traiter_donnees_avec_csv())
        choix = menu()

    elif choice== '2' :
        print(traiter_donnees_avec_json())
        choix = menu()
        
    elif choice == '3' :
        print(traiter_donnees_avec_xml())
        choix = menu()


    else :
        print("choix pas bon")
        choix = menu()



if choice =='4' :
    system("rm Donnees_Invalides_json.json")
    exit
