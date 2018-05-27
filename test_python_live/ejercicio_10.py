# Prueba 2
from funciones import *


suma = 0                # acumulador
cant = 0                # contador
cant_mucho_calor = 0    # contador para contar las temp, que hizo mucho calor
temp_alta = 0
temp_baja = 0
lista_temps = list()
lista_frio = list()
lista_calor = list()
lista_mucho = list()

while(True):
    temp = float(input("Temperatura:"))

    if(temp == -1000):
        break

    lista_temps.append(temp)

    cant += 1       # contando las temperaturas
    suma += temp    # sumando las temperaturas

    if(temp >= 1 and temp <= 15):
        print("Frío")
        lista_frio.append(temp)
    elif(temp >= 16 and temp <= 27):
        print("Calor")
        lista_calor.append(temp)
    elif(temp > 28):
        print("Mucho calor")
        cant_mucho_calor += 1
        lista_mucho.append(temp)

    if(cant == 1):
        # temp, es la primera temperatura
        temp_alta = temp
        temp_baja = temp
    else:
        if (temp > temp_alta):
            temp_alta = temp

        if (temp < temp_baja):
            temp_baja = temp

# Fuera del ciclo
promedio = suma / cant
print("El promedio de temperaturas es:",promedio)

if(promedio >= 20 and promedio <= 26):
    print("El promedio del clima es agradable")

print("Cantidad de temp's mucho calor:",cant_mucho_calor)
print("Temperatura más alta:",temp_alta)
print("Temperatura más baja:",temp_baja)

listar_temp("Todas las temperaturas", lista_temps)
listar_temp("Frio",lista_frio)
listar_temp("Calor", lista_calor)
listar_temp("Mucho calor", lista_mucho)


