from funciones import *

def ejercicio_1():
    print("Ejercicio 1")

    a = int(input("Ingrese a: "))
    b = int(input("Ingrese b: "))

    resultado = elevar(a,b)

    print(a,"elevado a",b,"es",resultado)

def ejercicio_2():
    print("Ejercicio 2")

    num_dia = int(input("Día de la semana:"))

    nombre_dia = nombre_semana(num_dia)

    print(nombre_dia)