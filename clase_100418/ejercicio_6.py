# Autor: Patricio Pérez Pinto
# Fecha: 10 de abril de 2018

cont_rojos = 0
cont_azules = 0
cont_sietes = 0
cont_unos = 0

while(True):
    nota = float(input("Nota: "))

    if(nota == -1):
        break

    if(nota >= 4):
        cont_azules = cont_azules + 1
    else:
        cont_rojos = cont_rojos + 1

    if(nota == 7):
        cont_sietes = cont_sietes + 1

    if(nota == 1):
        cont_unos = cont_unos + 1

print("Rojos: ",cont_rojos)
print("Azules: ",cont_azules)
print("Sietes: ",cont_sietes)
print("Unos: ",cont_unos)