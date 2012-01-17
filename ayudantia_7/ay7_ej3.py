paises = {}

def cuantos_en_comun(persona_1, persona_2):
	# El & es interseccion de conjuntos
	# Esta expresion retorna la cantidad de elementos en comun de los conjuntos
	return len(paises[persona_1] & paises[persona_2])

def main():
	persona = ''

	print 'Ingrese los datos iniciales'

	while persona != 'OK':
		persona = raw_input("Nombre persona (OK para terminar): ")

		if persona != 'OK':
			# Lo inicializamos como set() para que sea mutable
			paises[persona] = set()
			pais = ''
			
			while pais != 'OK':
				pais = raw_input("Pais (OK para terminar): ")

				if pais != 'OK':
					# Agregamos el pais al set
					paises[persona].add(pais)

	print "-- Datos iniciales --\n"
	print paises

	# El \n imprime un salto de linea
	print "\n-- Comparacion --"

	while True:
		persona_1 = raw_input("Persona 1 (OK para terminar): ")
		
		if persona_1 == 'OK':
			break
		
		persona_2 = raw_input("Persona 2 (OK para terminar): ")
		
		if persona_2 == 'OK':
			break

		print 'Tienen', cuantos_en_comun(persona_1, persona_2), 'paises en comun'


if __name__ == '__main__':
	main()