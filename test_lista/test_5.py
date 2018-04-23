carrito = list()

def agregar(nombre):
    carrito.append(nombre)
    print("Producto agregado!")

def eliminar(indice):
    del carrito[indice]
    print("Eliminado")

def listar():
    indice = 0
    print("---------------------")
    print("Listado de productos!")
    print("---------------------")
    for producto in carrito:
        print(indice," - ", producto)
        indice += 1
    print("---------------------")

def modificar(indice, nombre_nuevo):
    carrito[indice] = nombre_nuevo
    print("Actualizado!")

def main():
    while(True):
        listar()
        print("-----------")
        print("Menú")
        print("-----------")
        print("1.- Agregar producto")
        print("2.- Actualizar producto")
        print("3.- Eliminar producto por índice")
        opcion = int(input("[Ingrese su opción. Si es -1, el sw se cierra]"))

        if (opcion == -1):
            break

        if (opcion == 1):
            # crear
            print("Ingrese -1 para volver al menú")
            while(True):
                nombre = input("Ingrese nombre: ")

                if(nombre == "-1"):
                    break

                agregar(nombre)
        elif (opcion == 2):
            # actualizar

            indice = int(input("Índice: "))
            nombre_nuevo = input("Nombre nuevo: ")
            modificar(indice, nombre_nuevo)
        elif (opcion == 3):
            # eliminar
            indice = int(input("Índice: "))
            eliminar(indice)

main()
