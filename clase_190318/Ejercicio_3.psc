// Autor: Patricio Pérez
// Fecha: 19 de marzo de 2018

// Enunciado: Pedir 1 sueldo
// y dar como bono el 7% de
// dicho sueldo. Sea lo más
// específico posible.

Algoritmo Ejercicio_3
	Definir sueldo Como Real
	Definir monto_bono Como Real
	Definir porc_bono Como Real // 0.07
	Definir sueldo_final Como Real
	
	
	// Entrada
	Escribir "¿Cuál es su sueldo?: "
	Leer sueldo
	Escribir "¿Que porcentaje de bono posee?"
	leer porc_bono
	
	
	// Proceso
	porc_bono = porc_bono / 100
	monto_bono = sueldo * porc_bono
	sueldo_final = sueldo + monto_bono
	
	// Salida
	Escribir "Sueldo: $",sueldo
	Escribir "% de bono: ",(porc_bono*100),"%"
	Escribir "Bono: $", monto_bono
	Escribir "Sueldo total: $",sueldo_final
FinAlgoritmo
