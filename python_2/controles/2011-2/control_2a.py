# Control 2A

num1 = int(raw_input("Ingrese numero 1: "))
num2 = int(raw_input("Ingrese numero 2: "))
num3 = int(raw_input("Ingrese numero 3: "))

if num1 > num2:
	if num2 > num3:
		distancia = num1 - num3
	elif num1 > num3:
		