from traitement_csv  import traiter_donnees_avec_csv
from traitement_json import traiter_donnees_avec_json
from traitement_xml import traiter_donnees_avec_xml
from traitement import menu
from os import system


choice = menu()


while choice != '4' :

    if choice == 1 :
        traiter_donnees_avec_csv()
        choix = menu()

    elif choice== '2' :
        traiter_donnees_avec_json()
        menu()

        
    elif choice == '3' :
        traiter_donnees_avec_xml()
        menu()


    else :
        print("choix pas bon")
        menu()
    
