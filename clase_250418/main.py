from mensajes import *
from baseDeDatos import *

bienvenida()
intentos = 0 # contador
max_intentos = 3

while(True):
    if(max_intentos == 3):
        print("Son",max_intentos,"intentos")
    else:
        print("Le quedan", max_intentos, "intentos")

    rut = input("Rut:")
    password = input("Password:")

    nombre = verificar(rut, password)

    if(nombre != -1):
        mensaje_menu()
        print(nombre)
        break
    else:
        error()

        intentos += 1

        max_intentos -= 1

        if(intentos == 3):
            print("Error 404")
            break









