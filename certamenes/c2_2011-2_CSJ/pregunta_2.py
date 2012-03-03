def cantidad_de_artistas(dia):
	return len(artistas_por_dia[dia])

def nombre_primer_artista(dia):
	codigo_artista = artistas_por_dia[dia][0]

	for key, value in artistas.items():
		codigo, _, _ = value

		if codigo_artista == codigo:
			return key

	return None

def pais_origen_ultimo(dia):
	codigo_artista = artistas_por_dia[dia][-1]

	for key, value in artistas.items():
		codigo, pais, _ = value

		if codigo_artista == codigo:
			return pais

	return None

def tiempo_total(dia):

	total = 0

	for codigo_artista in artistas_por_dia[dia]:
		for key, value in artistas.items():
			codigo, _, duracion = value

			if codigo == codigo_artista:
				total += duracion
				break

	return total

####################
# Codigo de prueba #
####################

artistas = {
	# nombre: codigo, origen, duracion en minutos de la presentacion)
	'Marco Antonio': (1, 'Estados Unidos', 74),
	'Louis Michael': (2, 'Puerto Rico', 70),
	'Mariana Hernandez': (3, 'Chile', 40),
	'Los cuatro': (4, 'Chile', 25),
	'Metallico': (5, 'Estados Unidos', 45),
	'Yutu': (6, 'Irlanda', 80),
	'Justino Vivar': (7, 'Canada', 5)
}

artistas_por_dia = {
	# dia, orden de las presentaciones
	"Lunes": (1,4,3,6,2,5),
	"Martes": (2,5,1),
	"Miercoles": (3,6,2,4),
	"Jueves": (2,5)
}

dia = raw_input('Ingrese dia: ')
print 'Ese dia se presentaran', cantidad_de_artistas(dia), 'artistas'
print 'El primer artista del dia sera', nombre_primer_artista(dia)
print 'El ultimo artista del dia viene de', pais_origen_ultimo(dia)
print 'Ese dia el concierto completo durara', tiempo_total(dia),'minutos'