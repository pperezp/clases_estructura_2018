lista_edades = list()

#limite = int(input("Cuantas edades: "))

cont = 1
while(True):
    mensaje = "Edad ",cont,": "
    edad = int(input(mensaje))

    if(edad == -1):
        break

    lista_edades.append(edad)

    cont += 1

cont_may = 0
cont_men = 0

print("Listado de mayores:")
indice = 0
for edad in lista_edades:
    if(edad >= 18):
        cont_may += 1
        print(indice, "-", edad)
    indice += 1

print("Listado de menores:")
indice = 0
for edad in lista_edades:
    if(edad < 18):
        cont_men += 1
        print(indice, "-", edad)
    indice += 1

print("Mayores: ", cont_may)
print("Menores: ", cont_men)

mayor_edad = max(lista_edades)
menor_edad = min(lista_edades)

lista_edades.sort(reverse=True) # ordenar la lista de forma asc

print("Mayor edad: ", mayor_edad)
print("Menor edad: ", menor_edad)

print(lista_edades)



lista_nombres = list()

lista_nombres.append("Yenifer")
lista_nombres.append("Zarcelo")
lista_nombres.append("Zarcelo")
lista_nombres.append("Jose")

nom_max = max(lista_nombres)
nom_min = min(lista_nombres)

lista_nombres.sort()
print(lista_nombres)

print(nom_max)
print(nom_min)



print("-------------------------------")
print("CALCULO DEL PROMEDIO DE EDADES")
print("-------------------------------")
suma = sum(lista_edades)

print(suma)

cont = len(lista_edades)
promedio = suma / cont
print("Promedio: ", promedio)
