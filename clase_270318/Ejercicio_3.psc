Algoritmo Ejercicio_3
    Definir comprometen Como Entero
    Definir asistieron Como Entero
    Definir porc_alu_as Como Real
    Definir porc_alu_nf Como Real
	
    // Entrada
    Escribir "Cantidad de alumnos que QUIERE ir al asado: "
    Leer comprometen
    Escribir "Cantidad de alumnos que FUERÓN: "
    Leer asistieron
	
    // Proceso
    porc_alu_as = (asistieron * 100) / comprometen
    porc_alu_nf = 100 - porc_alu_as
	
	si(porc_alu_as > 80)
		Escribir "Curso BKN! :D"
	SiNo
		Escribir "Curso desconocido!"
	FinSi
	
	
    // Salida
    Escribir "% de alumnos que fue: ", porc_alu_as
    Escribir "% de alumnos que no fue: ", porc_alu_nf
FinAlgoritmo