def codificar(frase):
    frase = frase.lower()

    frase = frase.replace("a", "1")
    frase = frase.replace("e", "2")
    frase = frase.replace("i", "3")
    frase = frase.replace("o", "4")
    frase = frase.replace("u", "5")

    frase = frase.replace("á", "1")
    frase = frase.replace("é", "2")
    frase = frase.replace("í", "3")
    frase = frase.replace("ó", "4")
    frase = frase.replace("ú", "5")

    return frase

def decodificar(frase):
    frase = frase.lower()

    frase = frase.replace("1", "a")
    frase = frase.replace("2", "e")
    frase = frase.replace("3", "i")
    frase = frase.replace("4", "o")
    frase = frase.replace("5", "u")

    return frase