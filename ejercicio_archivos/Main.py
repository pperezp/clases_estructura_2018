from Contacto import *
from Archivo import *

class Main:

    def main(self):
        cont = 0

        nombreArchivo = input("Como se llama el archivo?:")

        archivo = Archivo(nombreArchivo)

        while(cont < 3):
            nombre = input("Nombre:")
            numero = input("Número:")

            contacto = Contacto(nombre, numero)
            archivo.escribir(contacto)
            cont += 1

m = Main()
m.main()