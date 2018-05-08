lista_nombres = list()

lista_nombres.append("Enrique")
lista_nombres.append("Iso")
lista_nombres.append("Pato")
lista_nombres.append("Erik")
lista_nombres.append("Flavio")
lista_nombres.append("Pablo")
lista_nombres.append("Coni")
lista_nombres.append("Pabli")

print("Cantidad:",lista_nombres.__len__())
print("-------------------------")
print("Lista de alumnos(Hacia abajo)")
print("-------------------------")
for nom in lista_nombres:
    print(nom)
print("-------------------------")