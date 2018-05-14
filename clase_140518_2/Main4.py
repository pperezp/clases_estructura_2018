from Producto import *

cont = 0
acumulador = 0

cantidad = int(input("Cuantos productos: "))

while(cont < cantidad):
    p = Producto()

    p.nombre = input("nombre: ")
    p.precio = int(input("precio: "))
    p.cantidad = int(input("cantidad: "))
    p.total = p.precio * p.cantidad

    print("El total es: ",p.total)

    acumulador += p.total

    cont +=1
print("Valor venta:$", acumulador)