"""
que tabla quiere ver: 3 --> tabla
Hasta --> 4             --> hasta

3x1 = 3
3x2 = 6
3x3 = 9
3x4 = 12

"""
tabla = int(input("Qué tabla? "))
hasta = int(input("Hasta? ")) #4

cont = 1
while(cont <= hasta):
    resultado = tabla * cont
    print(tabla , "x" , cont , "=" ,resultado)
    # print(str(tabla)+" x "+str(cont)+" = "+str(resultado))

    cont += 1