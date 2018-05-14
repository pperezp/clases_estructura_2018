# Desarrollar un sistema que permita
# Pedir un producto.
# Los datos del producto son nombre, precio
# y cantidad.
# Al finalizar el ingreso, mostrar el total.


from Producto import *

p1 = Producto()

p1.nombre = input("nombre: ")
p1.precio = int(input("precio: "))
p1.cantidad = int(input("cantidad: "))

p1.total = p1.precio * p1.cantidad
print("total es: ", p1.total)