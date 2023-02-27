from traitement_csv  import traiter_donnees_avec_csv
from traitement_json import traiter_donnees_avec_json
from traitement_xml import traiter_donnees_avec_xml
from traitement import menu
from os import system


choice = menu()

while choice != '4' :
    print("choix")
    if choice == '1' :
        print(traiter_donnees_avec_csv())
        choice = menu()

    elif choice== '2' :
        print(traiter_donnees_avec_json())
        choice = menu()
        
    elif choice == '3' :
        print(traiter_donnees_avec_xml())
        choice = menu()
    elif choice =='4' :
        print("sortir")
        


    else :
        print("choix pas bon !!!!!")
        choice = menu()



