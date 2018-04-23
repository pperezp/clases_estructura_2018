# Autor: Patricio Pérez Pinto
# Fecha: 10 de abril de 2018

# Ejercicio:
# Pedir "ETERNAMENTE" un nombre
# si el nombre es "joselito" dejar de pedir
# y mostrar la cantidad de intentos
from builtins import int

intentos = 0

while(True):
    nombre = input("Ingrese un nombre: ")
    nombre = nombre.lower()
    nombre = nombre.strip()

    if(nombre == "joselito"):
        break
    else:
        print("Intente de nuevo")
        intentos = intentos + 1

# fuera del ciclo
print("Acertó!!!! intentos: ",intentos)