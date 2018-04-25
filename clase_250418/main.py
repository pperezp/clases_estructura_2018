from mensajes import *
from baseDeDatos import *

bienvenida()
rut = input("Rut:")
password = input("Password:")

nombre = verificar(rut, password)
""" 
if(estaUsuario == True):
    mensaje_menu()
else:
    error()
"""
if(nombre == -1):
    error()
else:
    mensaje_menu()
    print(nombre)






