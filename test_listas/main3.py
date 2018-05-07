# Ingresar n sueldos y mostrar el promedio
# mostrar el listado de sueldos al final

limite = int(input("Cantidad de sueldos:"))
lista_sueldos = list()
suma = 0
cantidad = 0 # __len__
cont_vueltas = 0

while(True):
    sueldo = int(input("Sueldo:"))

    lista_sueldos.append(sueldo)

    cont_vueltas += 1

    if(cont_vueltas == limite): # if de corte
        break

print("Listado de sueldos")
for s in lista_sueldos:
    print(s)
    suma += s # sumando

cantidad = lista_sueldos.__len__()
promedio = suma / cantidad

print("Promedio: "+str(promedio))


