# Tratamos al numero como string para que
# sea mas simple
numero = raw_input("Numero: ")

# Esta variable guardara el numero invertido
numero_invertido = ''

# Recorremos el string que guarda el numero
# desde atras hacia adelante
for i in range(len(numero) - 1, -1, -1):
	# En cada iteracion, agregamos el caracter
	# actual del string a un nuevo string
	numero_invertido += numero[i]

# Finalmente, el numero queda invertido
print int(numero_invertido)