from baseDeDatos import *
from mensajes import *
from os import system
import sys

def main():
    so = sys.platform

    bienvenido()

    intentos = 0

    while(True):
        rut = input("Ingrese rut:")
        password = input("Ingrese pass:")

        nombre = verificar(rut, password)

        if(nombre != -1):
            break
        else:
            error()
            intentos += 1
            print("Intentos: ",intentos)

            if(intentos == 3):
                # Linux
                if(so == "linux"):
                    system("shutdown now")
                elif(so == "win32"):
                    system("shutdown -p")

    mensaje_menu(nombre)


main()