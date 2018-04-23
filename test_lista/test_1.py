#Declaración de una lista
edades = list()
nombres = list()
lista = []

# Añadir un elemento a la lista
edades.append(23)
edades.append(11)
edades.append(52)
edades.append(28)

nombres.append("Juanito Pérez")
nombres.append("Fabiola Muñoz")
nombres.append("Ricardo Pérez")
nombres.insert( "Pato Pérez")

lista.append(22)
lista.append("casa")
lista.append(2.3)

# Saber la cantidad de elementos
cantidad_edades = len(edades)
cantidad_nombres = len(nombres)
cantidad_lista = len(lista)

print("Existen",cantidad_nombres,"nombres!")
print("Existen",cantidad_edades,"edades!")
print("Existen",cantidad_lista,"elementos!")


# Mostrar los elementos de una lista
print("------------------")
print("Listado de nombres")
print("------------------")
for nom in nombres:
    print(nom)
print("------------------")
print()

print("------------------")
print("Listado de edades")
print("------------------")
for edad in edades:
    print(edad, end=' ')
print()
print("------------------")


print("------------------")
print("Listado")
print("------------------")
for elemento in lista:
    print(elemento)
print("------------------")


# Eliminando elementos de una lista
del lista[0]
del lista[0]

print("------------------")
print("Listado")
print("------------------")
for elemento in lista:
    print(elemento)
print("------------------")