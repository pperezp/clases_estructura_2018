from mensajes import *
from baseDeDatos import *

bienvenida()
rut = input("Rut:")
password = input("Password:")

estaUsuario = verificar(rut, password)

if(estaUsuario == True):
    mensaje_menu()
else:
    error()
