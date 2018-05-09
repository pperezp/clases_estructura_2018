def contar_mayores(lista_edades):
    cont = 0

    # recorrer, iterar
    for edad in lista_edades:
        if(edad >= 18):
            cont += 1

    return cont