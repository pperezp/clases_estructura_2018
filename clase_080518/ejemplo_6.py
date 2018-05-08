def contar_rojos(lista_notas):
    cont = 0

    for nota in lista_notas:
        if(nota < 4):
            cont += 1

    return cont

def contar_azules(lista_notas):
    azules = 0

    for n in lista_notas:
        if(n >= 4):
            azules += 1

    return azules

def mostrar_lista(lista):
    print(lista)

def main():
    lista_notas = list()

    lista_notas.append(6.3)
    lista_notas.append(6.5)
    lista_notas.append(6)
    lista_notas.append(1)

    mostrar_lista(lista_notas)
    rojos = contar_rojos(lista_notas)
    azules = contar_azules(lista_notas)

    print("Azules: ",azules)
    print("Rojos: ",rojos)

main()