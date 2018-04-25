# Verfica si el usuario existe o no
# entregándome como resultado (return)
# True o False
def verificar(rut, password):
    if(rut == "11-1" and password == "1234"):
        return "Camilo Vergara"
    elif(rut == "22-2" and password == "4321"):
        return "César Aros"
    elif(rut == "33-3" and password == "7816"):
        return "Marco Silva"
    else:
        return -1