age = int(raw_input('Edad: '))
weight = float(raw_input('Peso: '))
height = float(raw_input('Altura: '))

imc = weight / (height ** 2)

if age < 45:
	if imc < 22.0:
		risk = 'bajo'
	else:
		risk = 'medio'
else:
	if imc < 22.0:
		risk = 'medio'
	else:
		risk = 'alto'

print 'Tu riesgo es', risk