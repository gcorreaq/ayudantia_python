token = raw_input("Token: ")
size = int(raw_input("N: "))

# Con esto se crea un triangulo
for rows in range(1, size + 1):
	for spaces in range(size - rows):
		print ' ',

	for tokens in range((2 * rows) - 1):
		print token,
	
	print ''

# Y con esto, se crea la parte de abajo, creando un 'diamante'
for rows in range(size - 1, 0, -1):
	for spaces in range(size - rows):
		print ' ',

	for tokens in range((2 * rows) - 1):
		print token,

	print ''