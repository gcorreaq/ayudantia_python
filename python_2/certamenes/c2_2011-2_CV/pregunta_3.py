# encoding: utf-8

def obtener_digito_guia(patente):
	# Siempre se saca el penultimo, y el digito se
	# pasa a 'int' para comparar sin problemas los valores
	return int(patente[-2])

def esta_con_restriccion(digitos, dia, patente):	
	digito_guia = obtener_digito_guia(patente)

	# Si el digito esta en la tupla de digitos con restriccion
	# entonces esto retornara True. Caso contrario, False
	return digito_guia in digitos[dia]

def dias_con_restriccion(digitos, patente):
	digito_guia = obtener_digito_guia(patente)

	# Lista de dias
	dias = []

	# Se recorre el diccionario con las restricciones
	for dia, digitos_restringidos in digitos.items():
		# Si el digito_guia esta en los numeros
		# con restriccion...
		if digito_guia in digitos_restringidos:
			# Se agrega a la lista
			dias.append(dia)

	return dias

def dias_sin_restriccion(digitos, patente):
	digito_guia = obtener_digito_guia(patente)

	# Conjunto de dias
	dias = set()

	# Se recorre el diccionario con las restricciones
	for dia, digitos_restringidos in digitos.items():
		# Si el digito_guia no esta en los numeros
		# con restriccion...
		if digito_guia not in digitos_restringidos:
			# ... el dia se agrega al conjunto
			dias.add(dia)

	return dias

####################
# Código de prueba #
####################
digitos = {
	'lunes': (3, 4, 5, 6),
	'martes': (7, 8, 9, 0),
	'miercoles': (1, 2, 3, 4),
	'jueves': (5, 6, 7, 8),
	'viernes': (9, 0, 1, 2)
}

print esta_con_restriccion(digitos, 'lunes', 'BBDT35')
print dias_con_restriccion(digitos, 'BBDT35')
print dias_sin_restriccion(digitos, 'BBDT35')