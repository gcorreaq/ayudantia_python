for i in range(1, 11):
	actual = 0
	for j in range(1, 11):
		actual += i

		# Notar que la coma para evitar saltos de linea va siempre al final
		print '%(actual)3d' % { "actual": actual },

	print ''