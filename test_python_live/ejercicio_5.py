"""

Enunciado: pedir un sueldo
y mostrar lo siguiente:

    -> [250.000 y 350.000] --> bono --> 200.000
    -> [350.001 y 550.000] --> bono --> 100.000
    -> [550.001 y 650.000] --> bono --> 50.000
    -> > 650.000 --> bono --> 1
"""
bono = 250000
sueldo = int(input("Sueldo: "))

if(sueldo >= 250000 and sueldo <= 350000):
    bono = 200000
elif(sueldo >= 350001 and sueldo <= 550000):
    bono = 100000
elif(sueldo >= 550001 and sueldo <= 650000):
    bono = 50000
elif(sueldo > 650000):
    bono = 1

print("Su bono es:",bono)
print("Su sueldo es: "+str(sueldo))
total = sueldo + bono
print("El sueldo final es: "+str(total))