curso = list()

curso.append("Maxi")
curso.append("Toledo")
curso.append("Julius")
curso.append("Javier")
curso.append("Josele")
curso.append("Isolina")
curso.append("Pablo")

print("----------------------")
print("Listado del curso (Hacia el lado)")
print("----------------------")
print(curso)
print("----------------------")
print("Cantidad de alumnos:",curso.__len__())
print("----------------------")
print("Listado de alumnos (Hacia abajo)")
print("----------------------")
print(curso[0])
print(curso[1])
print(curso[2])
print(curso[3])
print(curso[4])
print(curso[5])
print(curso[6])
print("----------------------")

largo = curso.__len__()
primero = curso[0]
ultimo = curso[largo-1]

print("Primero: ",primero)
print("Último: ",ultimo)