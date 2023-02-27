dico1={'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333', 'g':'4', 'h':'44', 'i':'444', 'j':'5', 'k':'55','l':'555','m':'6','n':'66','o': '666', 'p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999','0':'A','1':'B','2':'C','3':'D','4':'E','5':'F','6':'G','7':'H','8':'I','9':'J',' ':'00', "'":"'", "(":")", ",":",",";":";",":":":","!":"!","?":"?"        }
dico2={}

#chaine=input("Donner votre Phrase ")
chaine="bonjour aly. j'ai 17 ans"
chaine1=[]

for i in range(len(chaine)):
    for key in dico1 :
        if chaine[i]==key :
            chaine1.append(dico1[key])

#mettons un 0 au cas ou deux lettre succesive se rencontre
code=[]
code.append(chaine1[0])
for i in range(1,len(chaine1)) :
    a=chaine1[i-1]
    b=chaine1[i]
    if a[len(a)-1]==b[0]:
        code.append(0)
    code.append(chaine1[i])

#affichage du code final    
for i in range(len(code)):
    print(code[i], end="")

