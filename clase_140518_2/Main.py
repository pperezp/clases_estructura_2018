# Sistema que pida el nombre y la edad
# y diga si es menor o mayor

# Programación Orientada a objetos --> Reglas
# Como debo programar

# Entidad --> Persona

from Persona import *

nom = "ricardo"
edad = 20

persona = Persona()

persona.nombre = input("Nombre: ")
persona.edad = int(input("Edad: "))

if(persona.edad < 18):
    print("Menor de edad")
else:
    print("Mayor de edad")