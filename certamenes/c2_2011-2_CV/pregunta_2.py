# enconding: utf-8

# Busca el idioma en el que fue escrito un libro.
def obtener_idioma(titulo_a_buscar):
	# Se recorre la coleccion de libros
	for libro in libros:
		titulo, autor, _ = libro

		if titulo == titulo_a_buscar:
			# Se empieza a buscar en los autores
			for key, value in datos_autores.items():

				# Si la llave es el nombre del autor buscado
				if key == autor:
					_, _, idioma = value

					# Se retorna el idioma
					return idioma

	# Si no se encontro nada, se retorna None
	return None

# Busca el autor de un libro
def obtener_autor(titulo_a_buscar):
	# Se recorre la coleccion de libros
	for libro in libros:
		titulo, autor, _ = libro

		# Si el titulo coincide con el buscado
		if titulo == titulo_a_buscar:
			# Se retorna el autor
			return autor

	# Si no se encontro nada, se retorna None
	return None

# Calcula la diferencia de años entre la publicacion de un libro
# y el fallecimiento de su autor
def calcular_annos_antes_de_morir(titulo_a_buscar):
	# Se recorre la coleccion de libros
	for libro in libros:
		titulo, autor, publicacion = libro

		# Si se encuentra el titulo buscado
		if titulo == titulo_a_buscar:
			# Se recorre la coleccion de autores
			for key, value in datos_autores.items():
				if key == autor:
					_, muerte, _ = value

					# Se retorna la diferencia entre el año de muerte
					# y el año de publicación del libro
					return abs(muerte[0] - publicacion)

	return None


####################
# Código de prueba #
####################
libros = [
	('Papelucho programador', 'Marcela Paz', 1983),
	('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
	('Raw_input y Julieta', 'William Shakespeare', 1597),
	('La tuplamorfosis', 'Franz Kafka', 1915)
]

datos_autores = {
	# autor: nacimiento, defuncion, idioma
	'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'ingles'),
	'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'aleman'),
	'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'espanol'),
	'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'espanol')
}

titulo = raw_input('Ingrese titulo del libro: ')
print 'El libro fue escrito en', obtener_idioma(titulo),
print 'por', obtener_autor(titulo)
print 'El autor fallecio', calcular_annos_antes_de_morir(titulo), 'años',
print 'despues de haber escrito el libro'