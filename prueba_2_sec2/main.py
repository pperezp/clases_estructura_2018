total_g = 0
empates = 0
cont_p = 0
cont_arg = 0
cont_enum = 1

while(True):
    cont_p += 1
    print("Partido Nº",cont_enum)
    cont_enum += 1
    pais_1 = input("Pais 1:")

    if(pais_1.lower() == "salir"):
        cont_p -= 1
        break

    goles_1 = int(input("Goles país 1:"))
    pais_2 = input("Pais 2:")
    goles_2 = int(input("Goles país 2:"))



    total_g += (goles_1 + goles_2)

    if(goles_1 == goles_2):
        empates += 1

    if (pais_1.lower() == "argentina" or pais_2.lower() == "argentina"):
        cont_arg += 1

print("Total de goles: ",total_g)
print("Empates: ",empates)
print("Partidos jugados: ", cont_p)
print("Partidos Argentina: ",cont_arg)