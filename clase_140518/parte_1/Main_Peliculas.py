from parte_1.Pelicula import *

p1 = Pelicula(
    111,
    "Matrix I",
    "Ciencia Ficción",
    "Todo espectador",
    "Español latino"
)

p2 = Pelicula(
    222,
    "Avengers Infinity War",
    "Ciencia Ficción",
    "Todo espectador",
    "Ingles"
)

lista_peliculas = list()

lista_peliculas.append(p1)
lista_peliculas.append(p2)

for pelicula in lista_peliculas:
    print("--------------------")
    print(pelicula.nombre)
    print(pelicula.genero)

print("--------------------")