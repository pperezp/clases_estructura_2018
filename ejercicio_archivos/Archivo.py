class Archivo:

    def __init__(self, nomArchivo):
        self.nom = nomArchivo

    # anexar al archivo, un contacto
    def escribir(self, contacto):
        file = open(self.nom, "a")

        file.write(contacto.nombre+"-"+contacto.numero+"\n")
        file.close()