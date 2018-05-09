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

from funciones import *

def main():
    lista = list()

    while(True):
        edad = int(input("Edad:"))

        if(edad == -1):
            break

        lista.append(edad)

    mayores = contar_mayores(lista)

    print("Listado de edades")
    for edad in lista:
        print(edad)

    print("Mayores: ",mayores)

main()

