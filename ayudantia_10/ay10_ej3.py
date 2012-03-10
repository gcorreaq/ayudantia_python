def transform_data(row):
	return map(int, row.strip().split(' '))

def suma_lineas(nombre_archivo):
	sumas = []
	archivo = open(nombre_archivo)

	for linea in archivo:
		numeros = transform_data(linea)
		sumas.append(sum(numeros))

	archivo.close()
	return sumas

# Esta funcion esta pensada para un
# numero indeterminado de columnas
def suma_columnas(nombre_archivo):
	columnas = []
	archivo = open(nombre_archivo)

	for linea in archivo:
		numeros = transform_data(linea)

		# Se crean listas por cada columna
		if len(columnas) == 0:
			for columna in range(len(numeros)):
				columnas.append([])

		numero_columna = 0

		# Cada numero va en una columna
		for numero in numeros:
			columnas[numero_columna].append(numero)
			numero_columna += 1

	archivo.close()
	return map(sum, columnas)

####################
# Codigo de prueba #
####################
archivo_prueba = 'numeros_ej3.txt'

print suma_lineas(archivo_prueba)
print suma_columnas(archivo_prueba)