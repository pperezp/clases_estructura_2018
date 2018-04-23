# reprobados, si esta reprobado, mensaje

reprobados = list()
aprobados = list()

reprobados.append("Max Moraga")
reprobados.append("Roberto Guzmán")
reprobados.append("Flavio Toro")
reprobados.append("Luis Arellano")

aprobados.append("Rodrigo Serrano")
aprobados.append("Alex Vargas")
aprobados.append("Camilo Vergara")
aprobados.append("Esteban Bravo")
aprobados.append("Juan Castillo")
aprobados.append("Jose Torres")

nombre = input("Ingrese su nombre:")
nombre = nombre.lower()

for n in reprobados:
    n = n.lower()
    if(n == nombre):
        print("Usted ha reprobado :|")
        break

for n in aprobados:
    n = n.lower()
    if(n == nombre):
        print("Usted aprobó! :D")
        break