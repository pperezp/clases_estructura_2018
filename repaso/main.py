"""
lista_jugadores = list()
jug = dict()

dorsal      dor
nombre      nom
país        pai
posición    pos

"""

lista_jugadores = list()

def cargar_jugadores():
    j1 = dict()
    j2 = dict()
    j3 = dict();
    j4 = dict();

    j1["dor"] = 10
    j1["nom"] = "Messi"
    j1["pai"] = "Argentina"
    j1["pos"] = "d"

    j2["dor"] = 7
    j2["nom"] = "Cristiano Ronaldo"
    j2["pai"] = "Portugal"
    j2["pos"] = "d"

    j3["dor"] = 8
    j3["nom"] = "Arturo Vidal"
    j3["pai"] = "Chile"
    j3["pos"] = "c"

    j4["dor"] = 7
    j4["nom"] = "Alexis Sánchez"
    j4["pai"] = "Chile"
    j4["pos"] = "c"

    lista_jugadores.append(j1)
    lista_jugadores.append(j2)
    lista_jugadores.append(j3)
    lista_jugadores.append(j4)

def pause():
    input("Presione enter para continuar...")

def limpiar():
    for i in range(1, 20, 1):
        print("")

def crear():
    limpiar()
    # Definir el nuevo diccionario (es un jugador)
    jug = dict()

    # Leer los datos que el usuario ponga
    jug["dor"] = int(input("Dorsal: "))
    jug["nom"] = input("Nombre: ")
    jug["pai"] = input("País: ")

    while(True):
        print("Posición:")
        print("a.- Portero")
        print("b.- Defensa")
        print("c.- Medio campo")
        print("d.- Delantero")

        jug["pos"] = input("Posición:")  # a, b, c, ó d
        jug["pos"] = jug["pos"].lower()

        if(
            jug["pos"] == "a" or
            jug["pos"] == "b" or
            jug["pos"] == "c" or
            jug["pos"] == "d"
        ):
            break
        else:
            print("Ingrese una posición válida: [a,b,c,d]")

    # Añadir ese "Jugador" (Diccionario) en la lista
    lista_jugadores.append(jug)
    print("Registro ok del jugador!")
    pause();

def listar():
    limpiar()

    if (lista_jugadores.__len__() == 0):
        print("No hay jugadores")
    else:
        print("-------------------------")
        print("Listado de jugadores")
        print("-------------------------")
        for j in lista_jugadores:
            posicion = ""

            if(j["pos"] == "a"):
                posicion = "Portero"
            elif (j["pos"] == "b"):
                posicion = "Defensa"
            elif (j["pos"] == "c"):
                posicion = "Medio campo"
            else:
                posicion = "Delantero"

            print("[" + str(j["dor"]) + "] "+j["nom"] + " - "+posicion+" de " + j["pai"])

        print("-------------------------")
    pause();

def buscar():
    limpiar()

    print("1.- Buscar por nombre o país")
    print("2.- Buscar por posición")
    op_buscar = int(input("Opción: "))

    if(op_buscar == 1):
        texto = input("Ingrese nombre de país ó nombre del jugador:")
        texto = texto.lower()


        existe = False
        for j in lista_jugadores:
            if (
                str(j["nom"].lower()).__contains__(texto) or
                str(j["pai"].lower()).__contains__(texto)
            ):
                existe = True
                posicion = ""

                if (j["pos"] == "a"):
                    posicion = "Portero"
                elif (j["pos"] == "b"):
                    posicion = "Defensa"
                elif (j["pos"] == "c"):
                    posicion = "Medio campo"
                else:
                    posicion = "Delantero"

                print("[" + str(j["dor"]) + "] " + j["nom"] + " - " + posicion + " de " + j["pai"])

        if(not existe):
            print("No se encontraron resultados!")
    elif(op_buscar == 2):
        print("Posición:")
        print("a.- Portero")
        print("b.- Defensa")
        print("c.- Medio campo")
        print("d.- Delantero")

        op_posicion = input("Posición: ")

        cont = 0
        for j in lista_jugadores:
            if(j["pos"] == op_posicion):
                cont += 1
                posicion = ""

                if (j["pos"] == "a"):
                    posicion = "Portero"
                elif (j["pos"] == "b"):
                    posicion = "Defensa"
                elif (j["pos"] == "c"):
                    posicion = "Medio campo"
                else:
                    posicion = "Delantero"

                print("[" + str(j["dor"]) + "] " + j["nom"] + " - " + posicion + " de " + j["pai"])
        print("Se han encontrado "+str(cont)+" jugadores")
    pause();

def eliminar():
    limpiar()

    if(lista_jugadores.__len__() == 0):
        print("No hay jugadores")
    else:
        print("-------------------------")
        print("Listado de jugadores")
        print("-------------------------")

        i = 1
        for j in lista_jugadores:
            print(str(i) + ".- " + j["nom"])
            i += 1

        print(str(i) + ".- Volver")

        print("-------------------------")

        indice = int(input("Ingrese el número del jugador a eliminar:"))

        if (indice != i):
            indice = indice - 1

            while (True):
                resp = input("¿Realmente desea eliminar? [s/n]: ")
                resp = resp.lower()

                if (resp == "s" or resp == "n"):
                    break
                else:
                    print("Ingrese s ó n.")

            if (resp == "s"):
                lista_jugadores.pop(indice)
                print("Jugador eliminado!")

    pause();


def menu():
    cargar_jugadores()

    while(True):
        limpiar()
        print("Menú de jugadores")
        print("1.- Crear")
        print("2.- Listar")
        print("3.- Buscar")
        print("4.- Eliminar")
        print("5.- Salir")

        op_menu = input("Opción:") # String

        if(op_menu == "5"):
            break
        elif (op_menu == "1"):
            crear()
        elif (op_menu == "2"):
            listar()
        elif (op_menu == "3"):
            buscar()
        elif (op_menu == "4"):
            eliminar()

menu()