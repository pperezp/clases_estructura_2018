def ciclo(limite, mensaje):
    # ciclo(3, "hola") --> hola hola hola
    # ???????????

    vueltas = 0
    while(True):
        vueltas += 1

        print(mensaje)

        if(limite == vueltas):
            break


ciclo(12, "puntos")
