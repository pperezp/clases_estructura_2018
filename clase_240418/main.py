from baseDeDatos import *
from mensajes import *

def main():
    bienvenido()
    rut = input("Ingrese rut:")
    password = input("Ingrese pass:")

    nombre = verificar(rut, password)

    if(nombre == -1):
        error()
    else:
        mensaje_menu(nombre)

main()