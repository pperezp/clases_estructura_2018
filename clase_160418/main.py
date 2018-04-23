# Autor: Patricio Pérez Pinto
# Fecha: 16 de abril de 2018

"""
Pedir x cantidad de edades con un CICLO
y mostrar la suma de ellas.
Además mostrar cuantos mayores de
edad existen.
"""

# Contador para mayores
c_may = 0

# Contador para menores
cont_men = 0

# Acumulador para edades
acu_edades = 0

# Contador de vueltas
vuelta = 0

limite = int(input("Cuantas edades quiere ingresar?"))

while(True):
    edad = int(input("Edad: "))

    if(edad >= 18):
        c_may = c_may + 1
        print("Es mayor de edad!")
    else:
        cont_men += 1
        print("Menor de edad!")

    # sumar las edades ingresadas
    # ac = ac + var
    acu_edades = acu_edades + edad

    # print("ACU: ",acu_edades)

    vuelta = vuelta + 1

    if(vuelta == limite):
        break

print("La suma de edades es: ",acu_edades)
print("Mayores de edad: ", c_may)
print("Menores de edad: ", cont_men)
print("Gracias por utilizar la app")