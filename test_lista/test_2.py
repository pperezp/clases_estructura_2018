lista_machos = list()

lista_machos.append("José")
lista_machos.append("Marcelo")
lista_machos.append("Martinez")
lista_machos.append("Rivas")
lista_machos.append("Golott")

print("Lista de machos!")
indice = 0 # contador para los índices
for nom in lista_machos:
    print(indice,"-",nom)
    indice += 1 # indice = indice + 1

id_borrar = int(input("Borrar? Ingrese el número: "))
del lista_machos[id_borrar]

print(lista_machos)

