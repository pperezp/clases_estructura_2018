lista_peliculas = list()

def cargar_peliculas():
    p1 = dict()
    p2 = dict()
    p3 = dict()
    p4 = dict()
    p5 = dict()

    p1["isan"] = "111"
    p1["nomb"] = "Película 1"
    p1["anio"] = "1000"
    p1["gene"] = "a"

    p2["isan"] = "222"
    p2["nomb"] = "Película 2"
    p2["anio"] = "2000"
    p2["gene"] = "b"

    p3["isan"] = "333"
    p3["nomb"] = "Película 3"
    p3["anio"] = "3000"
    p3["gene"] = "c"

    p4["isan"] = "444"
    p4["nomb"] = "Película 4"
    p4["anio"] = "4000"
    p4["gene"] = "Infantil"

    p5["isan"] = "5"
    p5["nomb"] = "La Montaña Sagrada"
    p5["anio"] = "1979"
    p5["gene"] = "Arte"

    lista_peliculas.append(p1)
    lista_peliculas.append(p2)
    lista_peliculas.append(p3)
    lista_peliculas.append(p4)
    lista_peliculas.append(p5)

def limpiar():
    cont = 0
    while(cont < 20):
        print()
        cont += 1

def crear():
    limpiar()
    print("Crear película")

    pelicula = dict() # pelicula = {}

    pelicula["isan"] = input("ISAN: ")
    pelicula["nomb"] = input("Nombre: ")
    pelicula["anio"] = input("Año: ")

    print("Género:")
    print("a.- Terror")
    print("b.- Comedia")
    print("c.- Acción")
    pelicula["gene"] = input("Ingrese opción:")

    lista_peliculas.append(pelicula)


def mostrar():
    limpiar()
    print("a.- Mostrar Todas las películas")
    print("b.- Mostrar por género")
    op_mostrar = input("Ingrese opción:")

    if(op_mostrar == "a"):
        print("----------------------------")
        print("Todas las película")
        print("----------------------------")
        for peli in lista_peliculas:
            print("ISAN:", peli["isan"])
            print("Nombre:", peli["nomb"])
            print("Año:", peli["anio"])

            if (peli["gene"] == "a"):
                print("Terror")
            elif (peli["gene"] == "b"):
                print("Comedia")
            elif (peli["gene"] == "c"):
                print("Acción")
            elif(peli["gene"] == "d"):
                print("Otros")

            print("----------------------------")
    elif(op_mostrar == "b"):
        print("a. Terror")
        print("b. Comedia")
        print("c. Acción")
        print("d. Otros")

        op_genero = input("Ingrese género:")

        print("----------------------------")
        print("Película según genero")
        print("----------------------------")
        for peli in lista_peliculas:
            if( peli["gene"] != "a" and
                peli["gene"] != "b" and
                peli["gene"] != "c" and
                op_genero == "d"):
                print(peli)
            elif(peli["gene"] == op_genero):
                print("ISAN:", peli["isan"])
                print("Nombre:", peli["nomb"])
                print("Año:", peli["anio"])

                if (peli["gene"] == "a"):
                    print("Terror")
                elif (peli["gene"] == "b"):
                    print("Comedia")
                elif (peli["gene"] == "c"):
                    print("Acción")


                print("----------------------------")


def buscar():
    limpiar()
    print("Buscar película")

def eliminar():
    limpiar()
    print("Eliminar películas")

def main():
    limpiar()
    cargar_peliculas()
    # Menú
    while(True):
        print("Menú")
        print("a.- Crear Película")
        print("b.- Mostrar Película")
        print("c.- Buscar Película")
        print("d.- Eliminar Película")
        print("e.- Salir")

        op_menu = input("Ingrese opción:")

        if(op_menu.lower().strip() == "e"):
            break
        elif(op_menu == "a"):
            crear()
        elif(op_menu == "b"):
            mostrar()
        elif(op_menu == "c"):
            buscar()
        elif(op_menu == "d"):
            eliminar()

main()