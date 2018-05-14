"""
nombre, edad sueldo

cuando el nombre sea salir

    --> Listados de nombres, sueldos y edades

Ademas mostrar el promedio de sueldos
    --> suma / cantidad
        acu  / cantidad de sueldos
               lista.__len__() --> cuantos items

y la cantidad de menores de edad
y la cantidad de personas llamadas luis astorga

con funciones ???? abierta
"""
from funciones import *

lista_nombres = list()
lista_edades = list()
lista_sueldos = list()

cont_men = 0
cont_luis = 0

while(True):
    nombre = input("Nombre:")

    if (nombre == "salir"):
        break

    lista_nombres.append(nombre)

    if(nombre.lower() == "luis astorga"):
        cont_luis += 1

    edad = int(input("Edad:"))
    lista_edades.append(edad)

    if(edad < 18):
        cont_men += 1

    sueldo = int(input("Sueldo:"))
    lista_sueldos.append(sueldo)

mostrar_lista(lista_nombres, "Nombres")
mostrar_lista(lista_sueldos, "Sueldos")
mostrar_lista(lista_edades, "Edades")

prom_sueldos = obtener_promedio(lista_sueldos)
print("El promedio de sueldos es:",prom_sueldos)

print("Menores de edad:",cont_men)
print("Luises Astorgas:",cont_luis)
