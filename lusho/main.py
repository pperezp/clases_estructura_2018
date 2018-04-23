# Autor: Patricio Pérez
# Fecha: 11 de abril de 2018

# lista: es un conjunto de datos
# de un mismo tipo, haciendo
# referencia con un sólo nombre.

sensibles = list()

sensibles.append("te lo pongo")
sensibles.append("te lo hago")
sensibles.append("te lo muestro")
sensibles.append("cometelo todo")
sensibles.append("lo teni abierto")
sensibles.append("dame la pasa")
sensibles.append("nos vamos a comer")
sensibles.append("te lo saco")
sensibles.append("tay caliente")
sensibles.append("te lo paso")
sensibles.append("me lo comi")
sensibles.append("te lo soplo")
sensibles.append("cabeza")

print("Frase: ")
frase = input()

# Búsqueda
for palabra in sensibles:
    if(frase.__contains__(palabra)):
        print("UUUUUUYYYYYYY....",palabra)




