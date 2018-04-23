lista_notas = list()

lista_notas.append(5.2)
lista_notas.append(2.5)
lista_notas.append(6.9)
lista_notas.append(4)
lista_notas.append(5.7)

cont_azules = 0
cont_rojos = 0

for nota in lista_notas:
    if(nota < 4):
        cont_rojos = cont_rojos + 1
    else:
        cont_azules = cont_azules + 1

print("Cantidad de rojos:", cont_rojos)
print("Cantidad de azules:", cont_azules)