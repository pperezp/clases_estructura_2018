Algoritmo Ejercicio_3
    Definir comprometen Como Entero
    Definir asistieron Como Entero
    Definir paa Como Real
    Definir panf Como Real
	
    // Entrada
    Escribir "Cantidad de alumnos que QUIERE ir al asado: "
    Leer comprometen
    Escribir "Cantidad de alumnos que FUERÓN: "
    Leer asistieron
	
    // Proceso
    paa = (asistieron * 100) / comprometen
    panf = 100 - paa
	
	si(paa >= 0 y paa <= 10)
		Escribir "Absolutamente caquita"
	SiNo
		si(paa > 10 y paa <= 20)
			Escribir "Medianamente caquita"
		SiNo
			si(paa > 20 y paa <= 50)
				Escribir "Parcialmente caquita"
			SiNo
				si(paa > 50 y paa <= 70)
					Escribir "Aceptable"
				SiNo
					si(paa > 70 y paa <= 80)
						Escribir "bien, se puede mejorar"
					SiNo
						si(paa > 80 y paa <= 90)
							Escribir "casi perfecto!"
						SiNo
							si(paa == 100)
								Escribir "curso perfecto!"
							SiNo
								si(paa > 90)
									Escribir "brigidos"
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	
    // Salida
    Escribir "% de alumnos que fue: ", paa
    Escribir "% de alumnos que no fue: ", panf
FinAlgoritmo