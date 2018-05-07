"""
Hasta ahora, en la prueba:
    - Ciclos --> while
    - Contadores, Acumuladores
    - PORCENTAJES
    - Funciones
    - if else
    - listas --> listas de nombres, listas
    de números, trabajo con listas (recorrer
    una lista, sumar sus números, ver el mayor
    el menor.)
"""

"""
def ejemplo_1():
    i = 0
    c = 1
    while(i <= 20):
        i += 2
        print(str(c)+") hola")
        c += 1

        if(i == 3):
            break

    print("Adios")
"""


def ejemplo_2():
    a = 2
    b = 3
    c = 0

    while(c != 6):
        a = a + 30
        b -= 20
        c += 2

        if(a == 30):
            a = 0

    print(a)
    print(b)
    print(c)

ejemplo_2()
