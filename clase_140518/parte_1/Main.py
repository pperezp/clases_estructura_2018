from parte_1.Juego import *

j1 = Juego(1, "Terraria", 5500, 100)
j2 = Juego(2, "PES 18", 21990, 300)
j3 = Juego(3, "Solitario Spider", 0, 900)

lista_juegos = list()

lista_juegos.append(j1)
lista_juegos.append(j2)
lista_juegos.append(j3)

for j in lista_juegos:
    print("----------------")
    print(j.id)
    print(j.nombre)
    print(j.precio)
    print(j.stock)

print("----------------")