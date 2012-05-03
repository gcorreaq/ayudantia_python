from numpy import *

def sumar_triangulo(matriz):
	filas = len(matriz)

	# Par
	if filas % 2 == 0:
		inicio = (filas / 2) - 1
		# Consideramos dos casillas al inicio
		fin = inicio + 2

	# Impar
	else:
		inicio = filas / 2
		# Solo una casilla considerada
		fin = inicio + 1

	# Siempre se parte en (filas / 2) redondeado
	# hacia abajo
	fila_inicio = (filas / 2)

	suma = 0

	for fila in range(fila_inicio, filas):
		rebanada = matriz[fila, inicio:fin]
		print rebanada
		suma += sum(rebanada)

		inicio -= 1
		fin += 1

	return suma

#####################
# Codigo de pruebas #
#####################

def main():
	a = array([[1, 7, 8, 9, 10, 3, 6],
			   [6, 7, 2, 5, 4, 9, 0],
			   [4, 6, 1, 5, 7, 0, 7],
			   [6, 7, 3, 3, 1, 0, 1],
			   [6, 9, 2, 0, 4, 9, 1],
			   [7, 1, 4, 5, 8, 1, 0],
			   [1, 0, 3, 5, 7, 7, 6]])

	print 'Matriz con N impar'
	print sumar_triangulo(a)

	b = array([[1, 7, 8, 9, 10, 3, 6, 8],
			   [1, 7, 8, 9, 10, 3, 6, 8],
			   [6, 7, 2, 5, 4, 9, 0, 3],
			   [4, 6, 1, 5, 7, 0, 7, 4],
			   [6, 7, 3, 1, 9, 0, 1, 3],
			   [6, 9, 3, 1, 2, 3, 1, 1],
			   [7, 8, 6, 4, 9, 1, 9, 0],
			   [3, 4, 2, 6, 8, 9, 0, 5]])

	print 'Matriz con N par'
	print sumar_triangulo(b)

if __name__ == '__main__':
	main()