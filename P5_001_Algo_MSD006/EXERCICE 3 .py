
chaine ="Aaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaacccccccccccaaaaaaaaaaaaaaaa.  BbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbW. nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnW. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA *#ZZ."
chainecorrect = ""
tab = []
phrase = ""
caractere=["'","(","-",")","!",":",";",',',"?","." ]

# j'enlève les espaces inutiles d'abord
chainecorrect=chainecorrect + chaine[0]
for i in range(1, len(chaine)):
    if (chaine[i-1] == " " and chaine[i] == " "):
        continue
    else:
        chainecorrect = chainecorrect + chaine[i]

for i in range(len(chainecorrect)):
    phrase = phrase + chainecorrect[i]
    if chainecorrect[i] in ['.', '!', '?']:
    
        if ('A' <= phrase[0] <= 'Z')  :
        
            phrase_correct = ""
            for j in range(len(phrase)):
                if 'a' <= phrase[j] <= 'z' or 'A' <= phrase[j] <= 'Z' or  '0' <= phrase[j] <= '9' or phrase[j] in caractere or phrase[j] == " " :
                    phrase_correct += phrase[j]
                else:
                    continue
            if len(phrase_correct) > 25:
                tab.append(phrase_correct)
        
        elif ('A' <= phrase[1] <= 'Z' and phrase[0]) :
            phrase_correct = ""
            for j in range(1, len(phrase)):
                if 'a' <= phrase[j] <= 'z' or 'A' <= phrase[j] <= 'Z' or  '0' <= phrase[j] <= '9' or phrase[j] in caractere or phrase[j] == " " :
                    phrase_correct += phrase[j]
                else:
                    continue
            if len(phrase_correct) > 25:
                tab.append(phrase_correct)


        phrase = ""

print("Les phrase corriger de votre texte sont: ")      
for phrase in tab :
    print(phrase)





