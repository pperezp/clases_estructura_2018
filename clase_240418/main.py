from baseDeDatos import *
from mensajes import *

def main():
    bienvenido()
    rut = input("Ingrese rut:")
    password = input("Ingrese pass:")

    userOK = verificar(rut, password)

    if(userOK):
        mensaje_menu()
    else:
        error()

main()