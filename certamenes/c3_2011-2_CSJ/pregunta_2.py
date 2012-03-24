def disponibilidad_de_sala(horario, dia_bloque, sala):
	archivo = open(horario)

	for linea in archivo:
		(_, _, dia1, dia2) = linea.strip().split(':')

		dia_bloque1, sala1 = dia1.split('/')
		dia_bloque2, sala2 = dia2.split('/')

		if (dia_bloque1 == dia_bloque or dia_bloque2 == dia_bloque) and (sala1 == sala or sala2 == sala):
			archivo.close()
			return False

	archivo.close()
	return True

def profesores_por_dia(horario):
	# Diccionario para guardar los dias y los
	# profesores que hacen clases en cada dia
	horarios = {}

	archivo = open(horario)

	for linea in archivo:
		(_, profesor, dia1, dia2) = linea.strip().split(':')

		dia_bloque1, _ = dia1.split('/')
		dia_bloque2, _ = dia2.split('/')

		# Cada dia en el diccionario tiene un conjunto
		# con los nombres de los profesores
		if dia_bloque1 in horarios:
			horarios[dia_bloque1].add(profesor)
		else:
			horarios[dia_bloque1] = { profesor }

		if dia_bloque2 in horarios:
			horarios[dia_bloque2].add(profesor)
		else:
			horarios[dia_bloque2] = { profesor }

	archivo.close()
	salida = open('profesores_por_dia.txt', 'w')

	for horario, profesores in horarios.items():
		lista_profesores = '/'.join(profesores)
		
		# Si la lista de profesores se quiere dejar igual que en el ejemplo
		# del certamen, descomentar la sgte linea
		#lista_profesores += '/'
		
		salida.write("{0}: {1}\n".format(horario, lista_profesores))

	salida.close()
	return None


def main():
	print disponibilidad_de_sala('horarios.txt', 'Martes 1-2', 'C201')
	profesores_por_dia('horarios.txt')

if __name__ == '__main__':
	main()