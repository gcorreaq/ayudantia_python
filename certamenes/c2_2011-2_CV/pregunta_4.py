# encoding: utf-8

from math import sqrt

def calcular_distancia(cliente, antena):
	c_x, c_y = cliente
	a_x, a_y = antena

	# Esta es la formula de distancia entre dos puntos
	return sqrt(((c_x - a_x) ** 2) + ((c_y - a_y) ** 2))

def mejor_antena(antenas, clientes, c):
	# Se buscan los datos del cliente 'c'
	for cliente in clientes:
		id_cliente, coord_cliente = cliente

		if id_cliente == c:
			# Se crea una lista para almacenar
			# las distancias a las antenas
			distancias_a_antenas = []

			for antena in antenas:
				id_antena, coords_antena = antena

				# Se calcula la distancia antena-cliente
				distancia = calcular_distancia(coord_cliente, coords_antena)

				# Si la distancia entre el cliente y la antena
				# es menor o igual que 3 Km...
				if distancia <= 3:
					registro = (distancia, id_antena)
				
					# ... se agrega a la lista
					distancias_a_antenas.append(registro)

			if len(distancias_a_antenas) > 0:
				# Se ordena la lista. Las menores distancias
				# quedaran al principio
				distancias_a_antenas.sort()
				# Se desempaqueta la primera tupla
				_, id_mejor_antena = distancias_a_antenas[0]

				return id_mejor_antena
			else:
				return None

####################
# Código de prueba #
####################
antenas = [('A1', (1, 7)), ('A2', (5, 2)), ('A3', (4, 8))]
clientes = [('C1', (1, 2)), ('C2', (4, 1)), ('C3', (3, 5)), ('C4', (3, 9)), ('C5', (5, 7))]
print mejor_antena(antenas, clientes, 'C4')
print mejor_antena(antenas, clientes, 'C1')