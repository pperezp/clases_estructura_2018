lista_nombres = list()
c = 0
limite = int(input("Cantidad de nombres:"))

while(c < limite):
    nombre = input("Nombre:")

    if(lista_nombres.__contains__(nombre)):
        print("Error, el nombre ya está")
    else:
        lista_nombres.append(nombre)
        c += 1

print("-----------------------")
print("Listado de curso")
print("-----------------------")

for nom in lista_nombres:
    print(nom)


print("-----------------------")