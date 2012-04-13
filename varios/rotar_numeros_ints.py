# Se pide el numero como string
numero = raw_input("Numero: ")
# Esta variable guardara el resultado
numero_inverido = 0

# Debemos calcular la posicion del valor mas grande
# Esto se hace en base a la cantidad de digitos del string
potencia = 10 ** (len(numero) - 1)

# Ahora el numero es transformado en entero
numero = int(numero)

# Mientras el numero sea mayor a cero...
while numero > 0:
	# Se saca un digito del numero, se multiplica
	# por la potencia actual para posicionarlo correctamente,
	# y se suma al numero invertido
	numero_inverido += (numero % 10) * potencia

	# Se elimina el digito de mas a la derecha
	numero /= 10
	# Se disminuye la potencia para posicionar
	# el siguiente digito donde corresponde
	potencia /= 10

print numero_inverido