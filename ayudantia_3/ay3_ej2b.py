num = int(raw_input("N: "))

f_0 = 0
f_1 = 1

if num == 0:
	print 'F0 =', f_0
elif num >= 1:
	print 'F0 =', f_0
	print 'F1 =', f_1

	actual = f_1
	anterior = f_0
	
	for i in range(2, num + 1):
		tmp = actual
		actual = actual + anterior
		anterior = tmp
	
		print 'F%(i)d = %(actual)d' % { "i": i, "actual": actual }