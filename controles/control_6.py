def frecuencia_uso_de_puentes(archivo):
	registros = open(archivo)
	puentes = {}

	for linea in registros:
		puente = linea.strip().split(';')[1]

		if puente in puentes:
			puentes[puente] += 1
		else:
			puentes[puente] = 1

	return puentes