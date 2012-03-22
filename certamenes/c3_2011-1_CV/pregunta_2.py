from numpy import *

def medias_moviles(serie, p):
	resultados = []

	for i in range((len(serie) - p) + 1):
		trozo = serie[i:i+p]
		resultados.append(sum(trozo) / p)

	return array(resultados)

def diferencias_finitas(serie):
	resultados = []

	for i in range(1, len(serie)):
		diferencia = serie[i] - serie[i - 1]
		resultados.append(diferencia)

	return array(resultados)

s = array([5, 2, 2, 8, -4, -1, 2])
print medias_moviles(s, 3)
print diferencias_finitas(s)