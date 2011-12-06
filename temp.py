certamen_1 = float(raw_input('C1: '))
certamen_2 = float(raw_input('C2: '))
nota_laboratorio = float(raw_input('NL: '))
nota_necesaria = (180/0.7) - certamen_1 - certamen_2 - (nota_laboratorio * 0.9) / 0.7
print 'Necesitas un', nota_necesaria, 'en el certamen 3'
