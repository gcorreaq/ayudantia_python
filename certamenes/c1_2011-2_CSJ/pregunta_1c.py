# Pueden descomentar los print para ver los cambios en los valores

i = 100
j = 2
g = ''
while i > j:
	i /= 2
	#print 'i:', i
	j *= 3
	#print 'j:', j
	if j % 2 == 0:
		#print 'Condicion verdadera'
		j += 1
		#print 'j:', j
	g += '*'
	#print 'g:', g
print g