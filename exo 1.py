myTable = [5,2,4,9,7]
stockage_valeur = 0


stockage_valeur = myTable[1]
myTable[1] = myTable[4]
myTable[4] = stockage_valeur

print(myTable)