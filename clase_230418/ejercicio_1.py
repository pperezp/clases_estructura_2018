# Fecha: 23 de abril 2018
# Autor: Patricio Pérez Pinto

# Pedir n edades, y muestre
# la cantidad de mayores de edad
# y la cantidad de menores además de
# el promedio de ambos

limite = int(input("Cuantas edades?"))
cont_may = 0
cont_men = 0
acu_may = 0
acu_men = 0

vueltas = 0
while(True):
    edad = int(input("Edad: "))
    vueltas += 1  # vueltas = vueltas + 1

    if(edad >= 18):
        cont_may += 1
        acu_may += edad
    else:
        cont_men += 1
        acu_men += edad

    if(vueltas == limite):
        break

print("Fuera del ciclo! chao")
print("Mayores: ",cont_may)
print("Menores: ",cont_men)

if(cont_may == 0):
    prom_may = 0
else:
    prom_may = acu_may / cont_may

if(cont_men == 0):
    prom_men = 0
else:
    prom_men = acu_men / cont_men

print("Promedio mayores:",round(prom_may, 4))
print("Promedio menores:",round(prom_men, 4))
