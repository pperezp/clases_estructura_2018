# Autor: Pato
# Fecha: 02 abril 2018

"""
Ingresar una temperatura y enviar los siguientes mensajes

entre 1 y 15 grados, mucho frío
entre 16 y 25 grados, tibio
entre 26 y 30 grados, calido
mas de 30, mucho calor
"""

temp = int(input("Temperatura: "))

if(temp >= 1 and temp <= 15):
    print("Mucho Frío! :'C")
else:
    if(temp >= 16 and temp <= 25):
        print("Tibio :| ")
    else:
        if(temp >= 26 and temp <= 30):
            print("Cálido C:'")
        else:
            if(temp > 30):
                print("Sofocad@! :'C")
            else:
                print("tAN HELAO QUE TAY JUAN!!")





            
        
