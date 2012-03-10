def obtener_palabra(numero_linea):
	linea_actual = 1
	archivo = open('lista_ahorcado.txt')

	for linea in archivo:
		if linea_actual == numero_linea:
			palabra = list(linea.strip())
			archivo.close()
			return palabra
		else:
			linea_actual += 1

	archivo.close()
	return None

def iniciar_lista(palabra):
	por_llenar = []

	for letra in palabra:
		if letra == ' ':
			por_llenar.append(' ')
		else:
			por_llenar.append('_')

	return por_llenar

def mostrar_adivinado(palabra):
	for letra in palabra:
		print letra,

	print '\n'

def comprobar(adivinar, adivinado, intento):
	indice = 0
	cambio = False

	for letra in adivinar:
		if letra == intento:
			adivinado[indice] = intento
			cambio = True

		indice += 1

	return adivinado, cambio

def sacar_parte(mono):
	if len(mono) == 0:
		return False

	parte = mono[0]
	del mono[0]

	return parte

def game():
	numero = int(raw_input('Numero entre 1 y 10: '))
	adivinar = obtener_palabra(numero)
	adivinado = iniciar_lista(adivinar)
	
	# Las vidas estan dadas por la cantidad de partes
	mono = ['pierna derecha', 'pierna izquierda', 'tronco', 'brazo derecho', 'brazo izquierdo', 'cabeza']

	print 'Empieza el juego!'

	while True:
		mostrar_adivinado(adivinado)
		intento = raw_input('Ingrese letra: ')
		adivinado, adivino = comprobar(adivinar, adivinado, intento)

		if not adivino:
			parte = mono[0]
			del mono[0]
			print 'Pierde', parte

			if len(mono) == 0:
				print 'Haz perdido el juego!'
				break
		elif adivinar == adivinado:
			mostrar_adivinado(adivinado)
			print 'Haz Ganado!'
			break

def main():
	print '======= El Ahorcado ======='
	print '\n'
	game()

if __name__ == '__main__':
	main()
