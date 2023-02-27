from Mes_fonctions import *


matrice_client = {}
entre = True

while entre == True :
    operateur = entre_operateur()
    info_client = entrer_info_client()
    ajout_client_dans_matrice(operateur, info_client)


    choix = input("Voulez vous entrer les informations d'un autre client? (o/n) ")
    if choix == "o" :
        entre = True
    else :
        entre = False


choice = menu_client()
while choice != '4' :
    if choice == "1" :
        afficher_client()
    elif choice == '2' :
        afficher_clients_par_operateur()
    elif choice == '3' :
        modifier_ajouter_client_telephone(matrice_client)
    else  :
        print("Choisis quelque chose")
        choice = menu_client()
    