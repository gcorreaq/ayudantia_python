num_1 = int(raw_input('Num 1: '))
num_2 = int(raw_input('Num 2: '))
num_3 = int(raw_input('Num 3: '))

#if num_1 < num_2 < num_3:
#	print num_1, num_2, num_3
#elif num_1 > num_2 > num_3:
#	print num_3, num_2, num_1

if num_1 < num_2:
	if num_1 < num_3:
		if num_2 < num_3:
			print num_1, num_2, num_3
		else:
			print num_1, num_3, num_2
	elif num_3 < num_2:
		print num_3, num_1, num_2
