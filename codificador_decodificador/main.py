from funciones import *

cont_decod = 0
cont_cod = 0

while(True):
    mensaje = input("Mensaje: ")

    if (mensaje.lower() == "salir"):
        print("se han codificado " + str(cont_cod) + " mensajes")
        print("se han decodificado " + str(cont_decod) + " mensajes")
        raise SystemExit  # salir del sw

    print("1.- Codificar mensaje")
    print("2.- Decodificar mensaje")
    print("3.- Invertir")
    op = int(input("Ingrese opción: "))

    if(op == 1):
        frase_cod = codificar(mensaje)
        print(frase_cod)
        cont_cod += 1
    elif(op == 2):
        frase_decod = decodificar(mensaje)
        print(frase_decod)
        cont_decod += 1
    elif(op == 3):
        inv = mensaje[::-1]
        print(inv)
    else:
        print("Error")


