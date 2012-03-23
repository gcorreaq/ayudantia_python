from numpy import *

def medias_moviles(serie, p):
	resultados = []

	# El indice 'i' tiene que llegar hasta 'p' posiciones
	# antes del final del arreglo. Se suma 1 para incluir
	# el ultimo elemento del arreglo.
	for i in range((len(serie) - p) + 1):
		# Se saca un slice de tamano 'p'
		trozo = serie[i:i+p]
		# Se agrega el promedio a la lista
		resultados.append(sum(trozo) / p)

	return array(resultados)

def diferencias_finitas(serie):
	resultados = []

	# Por simplicidad, se empieza con el indice en
	# el segundo elemento...
	for i in range(1, len(serie)):
		# ... asi, podemos hacer la resta del segundo
		# elemento con el primero, y asi sucesivamente
		diferencia = serie[i] - serie[i - 1]
		resultados.append(diferencia)

	return array(resultados)


####################
# Codigo de prueba #
####################

def main():
	s = array([5, 2, 2, 8, -4, -1, 2])
	print medias_moviles(s, 3)
	print diferencias_finitas(s)

if __name__ == '__main__':
	main()