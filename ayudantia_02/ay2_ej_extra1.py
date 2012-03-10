token = raw_input("Caracter: ")
rows = int(raw_input("Cant Filas: "))

for row in range(1, rows + 1):

	for spaces in range(rows - row):
		print ' ',

	for tokens in range(row):
		print token,

	print ''

for row in range(1, rows):

	for spaces in range(row):
		print ' ',

	for tokens in range(rows - row):
		print token,

	print ''