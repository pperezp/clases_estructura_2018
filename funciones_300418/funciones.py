# crear una función que pida n nombres
# pedir_nombres(10)

# Además debe contar a todos los nombres
# que contenga jose --> Jose --> josé --> replace

def ejercicio_1(cantidad):
    c = 1
    cont_jose = 0 # aun no se usa!

    while(True):
        #print("Ingrese nombre",c,":")
        #nombre = input()

        # no apto para cardiacos
        nombre = input("Ingrese nombre "+str(c)+":")

        nombre = nombre.lower() # dejamos el nombre en minúscula
        nombre = nombre.strip() # quitar espacios de los lados

        nombre = nombre.replace("é", "e")
        nombre = nombre.replace("ó", "o")

        if(nombre.__contains__("jose")):
            print("José salvaje encontrado!")
            cont_jose += 1

        if(c == cantidad):
            break

        c += 1

    print("Joses Salvajes: "+str(cont_jose))
