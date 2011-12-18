num = int(raw_input("N: "))

f_0 = 0
f_1 = 1

if 0 <= num <= 1:
	print num, 'es un numero de Fibonacci'
elif num > 1:

	actual = f_1
	anterior = f_0
	success = False
	
	while actual < num:
		tmp = actual
		actual = actual + anterior
		anterior = tmp

		if actual == num:
			print num, 'es un numero de Fibonacci'
			success = True

	if not success :
		print num, 'NO es un numero de Fibonacci'
else:
	print 'Solo numeros positivos'