def sumar(n1, n2):
    sum = n1 + n2
    print(n1,"+",n2,"=",sum) # 2 + 3 = 5

def restar(n1, n2):
    res = n1 - n2
    print(n1, "-", n2, "=", res)

def multiplicar(n1, n2):
    mul = n1 * n2
    print(n1, "*", n2, "=", mul)

def dividir(n1, n2):
    div = n1 / n2
    print(n1, "/", n2, "=", div)

def salir():
    print("Gracias por utilizar la app!")

def mostrar_menu():
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir")