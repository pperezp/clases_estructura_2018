# Autor: Patricio Pérez Pinto
# Fecha: 16 de abril de 2018

"""
Ingrese n sueldos
y ver cuantos tienen un sueldo
mínimo (< 270000) y además
muestre la suma de sueldos.
"""

# Contador para las vueltas
vuelta = 0

# Contador de sueldos mínimos
cont_min = 0

# Acumulador de sueldos
acu_sueldos = 0

limite = int(input("Cuantos sueldos?"))
while(True):
    sueldo = int(input("Sueldo: "))
    acu_sueldos += sueldo

    if(sueldo < 250000):
        #como cuento?
        cont_min += 1 # cont_min = cont_min + 1

    vuelta = vuelta + 1

    if(vuelta == limite):
        break

# output
print("Cantidad de sueldos pésimos: ",cont_min)
print("Suma de sueldos: ", acu_sueldos)