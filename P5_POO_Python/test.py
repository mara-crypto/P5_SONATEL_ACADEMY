# class Table:
#     def __init__(self):
#         pass

#     def ajoutertable(self,nom):

#         return nom
    
# table = Table()
# print(table.ajoutertable("fatou"))
# # print(Table.ajoutertable("fatou"))
date ="    FATOU.   "

date1 = ""
if date[0] != " " :
    date1 = date1 + date[0]
for i in range(1,len(date)) :
    if date[i-1] == " " and date [i] == " " :
        continue
    else :
        date1 = date1 + date[i] 

print(date1)

