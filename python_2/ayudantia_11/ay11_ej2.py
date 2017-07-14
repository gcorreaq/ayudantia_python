# Sudoku
from numpy import *

# Comprueba que todos los valores esten entre un rango
def comprobar_rango(data, min, max):
	return all(min <= data) and all(data <= max)

# Toma un arreglo bidimensional y lo pasa a un vector
def linealizar(matriz):
	return matriz.reshape((1, matriz.size))

# Revisa que cada numero sea unico por fila
# y columna
def revisar_unicos(data):
	for i in range(0, 9):
		fila = list(data[i, :])
		fila.sort()

		# Revisar filas
		for j in range(1, 9):
			if fila[j-1] >= fila[j]:
				return False

		columna = list(data[:, i])
		columna.sort()

		# Revisar columnas
		for j in range(1, 9):
			if columna[j-1] >= columna[j]:
				return False

	return True

# Revisa que cada region tenga numeros no repetidos
def revisar_regiones(data):
	for i in range(0, 9, 3):
		for j in range(0, 9, 3):
			region = data[i:i+3, j:j+3]

			numeros = list(linealizar(region))
			numeros.sort()

			for indice in range(1, len(numeros)):
				if numeros[indice-1] >= numeros[indice]:
					return False

	return True

# Comprueba que un tablero de sudoku este bien desarrollado
def solucion_es_correcta(sudoku):
	if comprobar_rango(sudoku, 1, 9) and revisar_unicos(sudoku) and revisar_regiones(sudoku):
		return True
	else:
		return False


####################
# Codigo de prueba #
####################
def main():
	sr = array([[4, 2, 6, 5, 7, 1, 3, 9, 8],
	            [8, 5, 7, 2, 9, 3, 1, 4, 6],
	            [1, 3, 9, 4, 6, 8, 2, 7, 5],
	            [9, 7, 1, 3, 8, 5, 6, 2, 4],
	            [5, 4, 3, 7, 2, 6, 8, 1, 9],
	            [6, 8, 2, 1, 4, 9, 7, 5, 3],
	            [7, 9, 4, 6, 3, 2, 5, 8, 1],
	            [2, 6, 5, 8, 1, 4, 9, 3, 7],
	            [3, 1, 8, 9, 5, 7, 4, 6, 2]])

	# Este siempre es True
	print 'Solucion correcta [Esperado: True] ->', solucion_es_correcta(sr)
	# Fuera de rango permitido
	sr[0, 0] = 19
	print 'Valor fuera de rango [Esperado: False] ->', solucion_es_correcta(sr)
	# Valor repetido en fila, columna y region
	sr[0, 0] = 9
	print 'Valor repetido en fila/columna/region [Esperado: False] ->', solucion_es_correcta(sr)

if __name__ == '__main__':
	main()
