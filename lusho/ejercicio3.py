# Tener una lista con notas --> float
# el usuario ingresa un comando

# ver notas
# y en ese momento se ve el listado de notas

lista_notas = list()

lista_notas.append(5.2)
lista_notas.append(2.5)
lista_notas.append(6.9)
lista_notas.append(4)
lista_notas.append(5.7)

comando = input("Comando:")

if(comando == "ver notas"):
    for nota in lista_notas:
        if(nota < 4):
            print(nota,"rojo")
        else:
            print(nota,"azul")
else:
    print("Comando desconocido")