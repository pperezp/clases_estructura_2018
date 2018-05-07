# Autor: Patricio Pérez Pinto
# Fecha: 2 de mayo de 2018

lista_notas = list()
cont_rojos = 0

# Notas de Ismael en Religión

lista_notas.append(7)
lista_notas.append(1.3)
lista_notas.append(7)
lista_notas.append(4)

"""
print(lista_notas)
print("La segunda nota de Ismael es:")
print(lista_notas[1])
print("La tercera nota de Ismael es: ")
print(lista_notas[2])
"""

# Recorrer la lista de notas del ismael

print("Listado de notas:")
cont = 0
for nota in lista_notas:
    cont += 1
    print(str(cont)+") "+str(nota))



