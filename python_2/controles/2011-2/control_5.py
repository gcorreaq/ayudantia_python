def comuna_con_menor_diferencia(temperaturas):
	menor_diferencia = None
	
	for comuna in temperaturas:
		nombre, extremas = comuna

		diferencia = extremas[1] - extremas[0]

		if menor_diferencia == None:
			menor_diferencia = diferencia
			comuna_menor_diferencia = nombre
		elif diferencia < menor_diferencia:
			menor_diferencia = diferencia
			comuna_menor_diferencia = nombre

	return menor_diferencia