from easy_input import get_int

# Definicion de funciones para el programa
def serie_multiplicacion(tope):

	resultado = 1

	for i in range(1, tope + 1):
		resultado *= i

	return resultado

# Inicio del programa
n = get_int("N: ")

print serie_multiplicacion(n)