# Ejercicio:
"""
Ingresar edades, hasta que
el usuario ingrese una edad
-1, guardar esas edades en una lista.
Además debe indicar la cantidad de mayores de edad.
y mostar todas las edades ingresadas

Todo esto programado con funciones. (Libre)

main() --> proyecto
contar_mayores(lista) --> retornar la cantidad de
mayores
"""

def contar_mayores(lista_edades):
    cont = 0

    # recorrer, iterar
    for edad in lista_edades:
        if(edad >= 18):
            cont += 1

    return cont

def main():
    lista = list()

    lista.append(18)
    lista.append(19)
    lista.append(18)
    lista.append(4)
    lista.append(1)
    lista.append(23)

    mayores = contar_mayores(lista)

    print(mayores)

main()

