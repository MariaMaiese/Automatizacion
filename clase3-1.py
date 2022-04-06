# Realizar un programa que permita adquirir productos en una ferreteria. 
# el sistema debe tener una lista de productos con sus precios
# el sistema debe permitir la seleccion del producto y calcular el valor a pagar (p x q)
#cuando el cliente desee no seguir comprando, mostrar el total de la compra
# luego consultar si el clinete desea despacho. Si es asi, calcule el costo del flere sehun la comuna de destino, no mas de 10 comunas.

productos = [[0,"candado", 5000],[1,"destornillador", 40000], [2,"tornillo",2000]]
comunas = [[0,"ñuñoa", 5000], [1,"santiago centro", 3000],[2,"la cisterna", 6000],[3,"la florida", 4000],[4,"puente alto", 5000]]

print("Bienvenido, estos son los productos de la ferretería:")
print ("{:<8} {:<15} {:<10}".format('Id','Descripcion','Precio'))

for i in productos:
    identificacion, descripcion, precio = i
    print ("{:<8} {:<15} {:<10}".format(identificacion, descripcion, precio))


total= 0
variable = 0
while variable !=-1:
    variable = int(input("Si desea comprar digite el numero identificador del producto, de lo contrario digite -1: "))
    
    if(variable > len(productos)-1) or (variable < -1):
         print("Producto no existente")

    else:
            producto_elegido = productos[variable][1]
            valor_producto_elegido = productos[variable][2]
            print("El producto elegido es: ", producto_elegido)
            
            cantidad = int(input("¿Qué cantidad? "))

            compra = valor_producto_elegido * cantidad
            print(f"El total de la compra de {producto_elegido} es {compra}")
            total = total + compra

            variable= int(input("Si desea comprar digite el numero identificador del producto, de lo contrario digite -1: "))

print("El total de la compra es: ", total)
respuesta_despacho = input("Desea despacho a domicilio? y/n ").lower()
total_despacho = 0

if(respuesta_despacho == "y"):
    print("Estas son las comunas a las que despachamos: ")
    print ("{:<8} {:<15} {:<10}".format('Id','Comuna','Precio Despacho'))

    for i in comunas:
        identificacion, comuna, precio = i
        print ("{:<8} {:<15} {:<10}".format(identificacion, comuna, precio))
    
    variable_comuna= int(input("Para despacho a domicilio digite el numero identificador de la comuna, de lo contrario digite -1: "))

    if((variable_comuna > len(comunas) -1) or variable_comuna < -1):
        print("Comuna no encontrada")
    elif(variable_comuna != -1):
        comuna_elegida = comunas[variable_comuna][1]
        valor_comuna_elegida = comunas[variable_comuna][2]
        print(f"La comuna elegida es: {comuna_elegida} y su valor es: {valor_comuna_elegida}")
        total_despacho = valor_comuna_elegida
        variable_comuna = int(input("Para finalizar, digite -1: "))
        if(variable_comuna == -1):
            total_final= total + total_despacho
            print("El total de la compra con despacho es: ", total_final)
else:
    print("El total de la compra sin despacho es: ", total)
    



