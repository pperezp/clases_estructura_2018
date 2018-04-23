lista_machos = list()

limite = int(input("Cuantos machos?:"))

cont = 1
while(True):
    nombre = input("Ingrese nombre del macho: ")

    lista_machos.append(nombre)

    if(cont == limite):
        break
    cont += 1

    print("Lista de machos!")
    indice = 0 # contador para los índices
    for nom in lista_machos:
        print(indice,"-",nom)
        indice += 1 # indice = indice + 1

id_borrar = int(input("Borrar? Ingrese el número: "))
del lista_machos[id_borrar]

print(lista_machos)