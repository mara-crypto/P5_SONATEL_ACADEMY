import numpy as np

#Créez un tableau NumPy unidimensionnel (1D) contenant les valeurs [1, 2, 3, 4, 5,6].
tab1d = np.array([1,2,3,4,5,6])

#Affichez la forme (shape) du tableau.
print(tab1d.shape) # renvoie (6,)

#Créez un tableau bidimensionnel (2D) à partir du tableau précédent en le remodelant en une matrice 2x3.
tab2d = np.array([[1,2,3],[4,5,6]]) # tab2d= tab1d.reshape(2,3)
print(tab2d.shape) # renvoie (2,3)

#Accédez à la valeur située à la deuxième ligne et troisième colonne du tableau 2D
print(tab2d[1][2])



################
################
# EXERCICE 2

#Créez un tableau NumPy contenant les nombres entiers de 1 à 5
tab1_5 = np.array([1,2,3,4,5])

# Affichez le type de données du tableau.
print(tab1_5.dtype) # Renvoie int64

# Convertissez le type de données du tableau en nombres à virgule flottante (float)
tab1_5 = tab1_5.astype(float)
print(tab1_5) #Renvoie [1. 2. 3. 4. 5.]

#Multipliez chaque élément du tableau par 2 et affichez le résultat
tab1_5 = tab1_5 * 2
print(tab1_5) #Renvoie [ 2.  4.  6.  8. 10.]




################
################
# EXERCICE 3

# 1. Créez deux tableaux NumPy contenant les valeurs [1, 2, 3] et [4, 5, 6].
tab1 = np.array([1, 2, 3])
tab2 = np.array([4, 5, 6])

# 2. Calculez la somme des deux tableaux.
som = np.sum([tab1, tab2])
print(som)  # Affiche 21


# 3. Calculez la différence entre les deux tableaux.
dif = np.subtract(tab1, tab2)
print(dif)

# 4. Multipliez les deux tableaux élément par élément.
prod = tab1 * tab2
print(prod) 

# 5. Calculez le produit scalaire des deux tableaux.
prodmat = np.dot(tab1,tab2)
print(prodmat)


################
################
# EXERCICE 4

# 1. Créez un tableau NumPy contenant les valeurs [1, 2, 3, 4, 5]
tabn = np.array([1,2,3,4,5])

# 2. Calculez la somme de tous les éléments du tableau.
som = np.sum(tabn)
print(som) #Renvoie 15

# 3. Calculez la moyenne des valeurs du tableau.
moy = np.mean(tabn)
print(moy) #Renvoie 3.0

# 4. Trouvez la valeur maximale et la valeur minimale du tableau.
maxtab = np.max(tabn)
print(maxtab)  #Renvoie 5

# 5. Calculez la racine carrée de chaque élément du tableau.
racine_carre = np.sqrt(tabn)
print(racine_carre) #Renvoie [1.         1.41421356 1.73205081 2.         2.23606798]