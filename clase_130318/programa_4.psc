// Autor: Patricio Pérez
// Fecha: 13 de marzo 2018

// Enunciado: Declarar un sueldo
// como entero, y mostrar el bono.
// El porcentaje de bono es 80%

// sueldo = $370.000
// el bono será de $296.000
// sueldo $666.000
Algoritmo programa_4
	// Definición de variables
	Definir sueldo Como Entero
	Definir valor_bono Como Entero
	// por_bono = porcentaje Bono
	Definir por_bono Como Real
	Definir sueldo_total Como Entero
	// Definición de variables
	
	// Inicializar --> Entrada
	sueldo = 1480000
	por_bono = 0.8
	// Inicializar --> Entrada
	
	// Proceso
	valor_bono = sueldo * por_bono
	sueldo_total = valor_bono + sueldo
	// Proceso
	
	// Salida
	Escribir "--------------------------------"
	Escribir "Sueldo inicial: ", sueldo
	Escribir "Porcentaje de bono: ", por_bono
	Escribir "BONO: ", valor_bono
	Escribir "--------------------------------"
	Escribir "Sueldo TOTAL: ", sueldo_total
	Escribir "--------------------------------"
	// Salida
	
FinAlgoritmo
