listaAm=[]

listaPm=[]

x = 0

for x in range(4):
    sueldoAm= int(input('Ingrese el sueldo ' + str(x+1)+ ": "))
    listaAm.append(sueldoAm)
    sueldoPm=int(input('Ingrese el sueldo ' + str(x+1)+ ": "))
    listaPm.append(sueldoPm)


print(listaAm)
print(listaPm)