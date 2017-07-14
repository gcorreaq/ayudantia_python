# Segunda alternativa de solucion

from numpy import *

# Para cumplir con lo pedido en el enunciado
A = array(['C','E','N','I','T'])
B = array(['P','O','L','A','R'])

def encriptar(palabra):
	palabra = palabra.upper()
	nueva_palabra = ''

	# Transformamos los arreglos en listas
	# para despues usar la funcion index()
	cenit = list(A)
	polar = list(B)

	for letra in palabra:
		# Si la letra esta en la lista...
		if letra in cenit:
			# ... usamos la funcion index para encontrar el indice
			# en donde esta la letra...
			indice = cenit.index(letra)
			# Y corresponde al mismo indice de la letra que tenemos
			# que reemplazar
			reemplazo = polar[indice]
		elif letra in polar:
			indice = polar.index(letra)
			reemplazo = cenit[indice]
		else:
			# No hay cambio
			reemplazo = letra

		# Se agrega el nuevo caracter
		nueva_palabra += reemplazo

	return nueva_palabra


####################
# Codigo de prueba #
####################

def main():
	print encriptar('Programacion')

if __name__ == '__main__':
	main()
