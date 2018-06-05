total_goles = 0
empates = 0
part_j = 0 # contador de partidos jugados
cont_arg = 0
cont_p = 1

while(True):
    print("Partido Nº",cont_p)
    cont_p += 1
    pais_1 = input("País 1: ")

    if(pais_1.lower() == "salir"):
        break

    gol_1 = int(input("Goles del País 1: "))
    pais_2 = input("País 2: ")
    gol_2 = int(input("Goles del País 2: "))

    total_goles += gol_1
    total_goles += gol_2

    if(gol_1 == gol_2):
        empates += 1

    part_j += 1

    if(pais_1.lower() == "argentina"):
        cont_arg += 1
    elif(pais_2.lower() == "argentina"):
        cont_arg += 1


print("Total de goles del mundial:", total_goles)
print("Empates: ",empates)
print("Partidos jugados: ", part_j)
print("Partidos de Argentina:", cont_arg)