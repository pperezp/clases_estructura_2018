lista_precios = list()
total = 0

while(True):
    cant = int(input("cantidad de productos: "))

    if(cant ==-1 ):
        break

    precio = int(input("Precio:"))
    pro_total = cant * precio
    lista_precios.append(pro_total)



for precio in lista_precios:
    total += precio

print("El total de la compra es:", total)