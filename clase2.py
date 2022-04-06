sueldos=[]

x=0
promedio =0
total = 0

for x in range(5):
    valor = int(input("ingrese el sueldo: " + str(x+1)))
    sueldos.append(valor)
    total = total + valor

print(sueldos)

promedio = total / len(sueldos)
print(promedio)