chaine=str(input("donner une chaine1:  "))
chaine1=""

chaine1 = chaine1 + chaine[0]
for i in range (1,len(chaine)):
        if (chaine[i-1]==" " and chaine[i]==" "):
            continue
        else :
            chaine1=chaine1+chaine[i]
print(chaine1)
