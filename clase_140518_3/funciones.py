def mostrar_lista(lista, titulo):
    print("-------------------------")
    print("Listado de",titulo)
    print("-------------------------")
    for x in lista:
        print(x)
    print("-------------------------")

def obtener_promedio(lista):
    acu = 0

    for sueldo in lista:
        acu += sueldo

    promedio = acu / lista.__len__()

    return promedio