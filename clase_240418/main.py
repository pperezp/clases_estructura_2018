from baseDeDatos import *
from mensajes import *

def main():
    bienvenido()

    while(True):
        rut = input("Ingrese rut:")
        password = input("Ingrese pass:")

        nombre = verificar(rut, password)

        if(nombre != -1):
            break
        else:
            error()

    mensaje_menu(nombre)

main()