# Autor: Patricio Pérez Pinto
# Fecha: 2 de mayo de 2018

lista_edades = list()

# promedio de edades (suma / cantidad)
suma = 0

lista_edades.append(12)
lista_edades.append(20)
lista_edades.append(21)
lista_edades.append(19)
print("-------------------------")
print("Las edades")
for e in lista_edades:
    print(e)
print("-------------------------")

for edad in lista_edades:
    suma += edad
    print("La suma parcial es: "+str(suma))

print("-------------------------")
promedio = suma / lista_edades.__len__()
print("El promedio es: "+str(promedio))
print("La cantidad de edades es: "+str(lista_edades.__len__()))
print("-------------------------")

