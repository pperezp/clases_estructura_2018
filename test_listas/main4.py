# Ingresar sueldos
# hasta que el sueldo sea -1
# y mostrar el promedio
# mostrar el listado de sueldos al final
#

lista_sueldos = list()
suma = 0
cantidad = 0 # __len__
while(True):
    sueldo = int(input("Sueldo:"))

    if(sueldo == -1): # if de corte
        break

    lista_sueldos.append(sueldo)

print("Listado de sueldos")
for s in lista_sueldos:
    print(s)
    suma += s # sumando

cantidad = lista_sueldos.__len__()
promedio = suma / cantidad

print("Promedio: "+str(promedio))



