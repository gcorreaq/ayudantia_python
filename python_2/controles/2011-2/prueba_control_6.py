import sys

def main():
	# Si viene un argumento, se asume que es el nombre de un archivo
	if len(sys.argv) > 1:
		import_name = sys.argv[1]
		# Se importa, omitiendo la extension del archivo
		control = __import__(import_name[:len(import_name) - 3])
	else:
		print "ERROR"
		return

	print "Puentes"
	print control.frecuencia_uso_de_puentes('datos_control_6.txt')

if __name__ == '__main__':
	main()