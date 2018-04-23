# Autor: Patricio Pérez Pinto
# Fecha: 10 de abril de 2018

cont_mujeres = 0
cont_hombres = 0

while(True):
    sexo = input("mujer o hombre?")

    if(sexo == "h"):
        cont_hombres = cont_hombres + 1
    else:
        if(sexo == "m"):
            # cont_mujeres = cont_mujeres + 1
            cont_mujeres += 1

    if(sexo == "s"):
        break

print("Mujeres: ",cont_mujeres)
print("Hombres: ",cont_hombres)