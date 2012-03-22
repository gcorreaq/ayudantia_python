
def main():
	votaciones = open('votaciones.txt')
	condorito = open('condorito.txt', 'w')
	tremebunda = open('tremebunda.txt', 'w')
	resultados = open('resultados.txt', 'w')

	contador = 0

	s = {
		'Norte': {
			'condorito': 0,
			'tremebunda': 0
		},
		'Centro': {
			'condorito': 0,
			'tremebunda': 0
		},
		'Sur': {
			'condorito': 0,
			'tremebunda': 0
		}
	}

	for l in votaciones:
		contador += 1

	votaciones.close()
	votaciones = open('votaciones.txt')

	for i in range(contador / 2):
		linea = votaciones.readline().strip()

		if linea != '':
			candidato = linea
			sector = votaciones.readline().strip()

			if candidato == 'A':
				# Tremebunda
				tremebunda.write(candidato + '\n')
				tremebunda.write(sector + '\n')

				if sector == 'Norte':
					s['Norte']['tremebunda'] += 1
				elif sector == 'Centro':
					s['Centro']['tremebunda'] += 1
				elif sector == 'Sur':
					s['Sur']['tremebunda'] += 1

			else:
				# Condorito
				condorito.write(candidato + '\n')
				condorito.write(sector + '\n')

				if sector == 'Norte':
					s['Norte']['condorito'] += 1
				elif sector == 'Centro':
					s['Centro']['condorito'] += 1
				elif sector == 'Sur':
					s['Sur']['condorito'] += 1
		else:
			return None

	condorito.close()
	tremebunda.close()
	votaciones.close()

	resultados.write('Sector sur\n')
	resultados.write('Dona Tremebunda ' + str(s['Sur']['tremebunda']) + ' votos\n')
	resultados.write('Condorito ' + str(s['Sur']['condorito']) + ' votos\n')
	resultados.write('Sector centro\n')
	resultados.write('Dona Tremebunda ' + str(s['Centro']['tremebunda']) + ' votos\n')
	resultados.write('Condorito ' + str(s['Centro']['condorito']) + ' votos\n')
	resultados.write('Sector norte\n')
	resultados.write('Dona Tremebunda ' + str(s['Norte']['tremebunda']) + ' votos\n')
	resultados.write('Condorito ' + str(s['Norte']['condorito']) + ' votos\n')

	resultados.close()

if __name__ == '__main__':
	main()