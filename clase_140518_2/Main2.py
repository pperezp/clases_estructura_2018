# Pedir un nombre de un alumno
# y sus notas (tres notas)

# al finalizar, sacar promedio del alumno
# POO

from Alumno import *

# Creo un objeto Alumno --> Instanciar
# Instanciando a la clase Alumno
alum = Alumno()

alum.nombre = input("Nombre: ")
alum.nota_1 = float(input("Nota 1:"))
alum.nota_2 = float(input("Nota 2:"))
alum.nota_3 = float(input("Nota 3:"))

# promedio = suma / 3
suma = alum.nota_1 + alum.nota_2 + alum.nota_3
alum.promedio = suma / 3
alum.promedio = round(alum.promedio, 1)


print("Promedio de",alum.nombre,":",alum.promedio)

if(alum.promedio >= 4):
    print("Aprobó :D")
else:
    print("Reprobó :C")


