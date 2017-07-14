# Esta solucion asume como entrada todos los numeros

numbers = raw_input("Numeros: ")
actual = 0

for i in range(len(numbers)):
	number = int(numbers[i])

	if number == 1:
		print 'Usted perdio'
		break
	elif actual != number:
		actual = number
		equals_count = 1
	else:
		equals_count += 1

		if equals_count == actual:
			print 'Usted gano'
			break