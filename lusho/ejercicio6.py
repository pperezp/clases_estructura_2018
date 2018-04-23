"""
Pedir 5 notas con un ciclo y
determinar la cantidad de rojos y azules
"""
rojos = 0
azules = 0
vueltas = 0 # contador --> cuenta las vueltas

while(True):
    vueltas = vueltas + 1

    # proceso
    nota = float(input("Nota: "))

    if(nota >= 4):
        azules = azules + 1
    else:
        rojos = rojos + 1
    # proceso

    if(vueltas == 4):
        break

print("Rojos: ", rojos)
print("Azules: ", azules)
