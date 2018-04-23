# Autor: Patricio Pérez
# Fecha: 03 de abril de 2018

num1 = float(input("Ingrese num 1: "))
num2 = float(input("Ingrese num 2: "))

print("----------------------")
print("App. principal")
print("----------------------")
print("Opciones:")
print("a) Sumarlos")
print("b) Restarlos")
print("----------------------")

opcion = input("Ingrese opción:")
opcion = opcion.strip()

if(opcion == "a" or opcion == "A"):
    suma = num1 + num2
    print("La suma es: ", suma)
else:
    if(opcion == "b" or opcion == "B"):
        resta = num1 - num2
        print("La resta es:", resta)
