myTable = [5,2,4,9,7]
plusGrand =[4]
stockage_valeur = 0

for i in range(len(myTable)):
    if (myTable[1]>myTable[0]):
    stockage_valeur = myTable[1]
    myTable[1] = myTable[i+1]
    myTable[i+1] = stockage_valeur

    
        
        

print(myTable)

#i wanna die, nique sa mère la pute

#quand le chiffre est plus grand que celui d'avant il doit aller a la fin du tableau

"""indice = 0
lePlusPetit = myTable[0]

for i in range (len(myTable)):
    if (lePlusPetit > myTable[i]):
        lePlusPetit = myTable[i]
        indice = i

indice = myTable.pop(indice)  


myTable.insert(0,indice) 


print(myTable)"""
