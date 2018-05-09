"""
Supermercado:
    Cajero:
        - Ingresar precios hasta que sea -1
            al finalizar mostrar el total de compra


"""

total = 0 # acumulador

while(True):
    precio = int(input("Ing. Precio: "))

    if(precio == -1):
        break

    total += precio

print("Total: ",total)