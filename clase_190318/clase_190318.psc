// Autor: Patricio Pérez
// Fecha: 19 de marzo de 2018

// Ejercicio:
// Pedir el año de nacimiento
// y el programa debe decir
// que edad tienes.

Algoritmo clase_190318
	// Definir las variables
	Definir anio_nac Como Entero // nac = nacimiento
	Definir anio_act Como Entero
	Definir edad Como Entero
	
	//anio_act = 2018
	
	Escribir "¿Año actual? :"
	Leer anio_act
	
	// Pedir al usuario el año de nacimiento
	Escribir "¿En qué año nació?: "
	Leer anio_nac
	
	// Proceso: Resta del año actual
	// menos el año de nacimiento
	edad = anio_act - anio_nac
	
	// Enviar un mensaje al usuario
	// con esa edad
	Escribir "Según mis cálculos, usted"
	Escribir "debería tener ",edad," años"	
	Escribir "Su año de nacimiento fue ",anio_nac
FinAlgoritmo
