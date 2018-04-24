# Fecha: 23 de abril 2018
# Autor: Patricio Pérez Pinto

# Realizar una calculadora con funciones
# sumar, restar, divi, mult

from funciones import *

def programa():
    while(True):
        n1 = int(input("n1:"))
        n2 = int(input("n2:"))

        mostrar_menu()

        op = int(input("Ingrese opción:"))

        if (op == 1):
            sumar(n1, n2)
        elif (op == 2):
            restar(n1, n2)
        elif (op == 3):
            multiplicar(n1, n2)
        elif (op == 4):
            dividir(n1, n2)
        elif(op == 5):
            salir()
            break

        # print("Gracias por usar esta app tierna")


programa()