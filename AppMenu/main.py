lista_chistes = list()

def crear():
    chiste = dict() # chiste = {}


    while(True):
        chiste["autor"] = input("Nombre del autor del chiste:")

        if(chiste["autor"].strip() != ""):
            break
        print("[ERROR]: Por favor escriba un nombre")


    chiste["anio"] = input("Año:")

    while(True):
        print("Tipo de chiste")
        print("a.- Chiste corto")
        print("b.- Doble sentido")
        print("c.- Chiste fome")
        op_tipo = input("Ingrese un tipo (a,b,c):")
        op_tipo = op_tipo.lower().strip()

        if(op_tipo == "a" or op_tipo == "b" or op_tipo == "c"):
            break

    chiste["tipo"] = op_tipo
    chiste["contenido"] = input("Escriba el chiste:")

    lista_chistes.append(chiste)

def mostrar():
    print("a.- Mostrar todos los chistes")
    print("b.- Mostrar chistes por tipo")
    print("c.- Mostrar chistes por año")
    op_mostrar = input("Ingrese opción:")

    if(op_mostrar == "a"):
        print("----------------------------")
        print("Listado de TODOS los chistes")
        print("----------------------------")

        for chi in lista_chistes:
            print("Autor:",chi["autor"])
            print("Año:",chi["anio"])

            if(chi["tipo"] == "a"):
                print("Tipo: Chiste corto")
            elif(chi["tipo"] == "b"):
                print("Tipo: Doble sentido")
            else:
                print("Chiste fome")

            print("Chiste: ")
            print(chi["contenido"])
            print("----------------------------")

    elif(op_mostrar == "b"):
        print("a.- Corto")
        print("b.- Doble Sentido")
        print("c.- Fome")
        op_tipo = input("Ingrese opción:")

        for chi in lista_chistes:
            if(chi["tipo"] == op_tipo):
                print("Autor:", chi["autor"])
                print("Año:", chi["anio"])

                if (chi["tipo"] == "a"):
                    print("Tipo: Chiste corto")
                elif (chi["tipo"] == "b"):
                    print("Tipo: Doble sentido")
                else:
                    print("Chiste fome")

                print("Chiste: ")
                print(chi["contenido"])
                print("----------------------------")



    elif(op_mostrar == "c"):
        anio = input("Ingrese el año:")
        # ???
def buscar():
    print("Buscar")

def eliminar():
    print("Eliminar")

def main():
    while(True):
        print("-----------------------")
        print("      Chistes 2018     ")
        print("-----------------------")
        print("a.- Crear un chiste    ")
        print("b.- Mostrar chistes    ")
        print("c.- Buscar chiste      ")
        print("d.- Eliminar           ") # Fluvio?
        print("e.- Salir              ")
        op_menu = input("Ingrese opción:")

        op_menu = op_menu.lower().strip()

        if(
            op_menu == "e"
            or op_menu == "salir"
            or op_menu == "chaito"
            or op_menu == "exit"
        ):
            break
        elif(op_menu == "a"):
            crear()
        elif(op_menu == "b"):
            mostrar()
        elif(op_menu == "c"):
            buscar()
        elif(op_menu == "d"):
            eliminar()
        else:
            print("\""+op_menu+"\" no existe")
main()