money = int(raw_input("Dinero: "))

remaining = money
item = -1

while item != 0:
	item = int(raw_input("Item (cero para terminar): "))

	# Sopaipillas
	if item == 1:
		print 'Una sopaipilla -> $100'
		remaining -= 100
	# Yogurt
	elif item == 2:
		print 'Un yogurt -> $200'
		remaining -= 200
	# Completo italiano
	elif item == 3:
		print 'Un italiano -> $500'
		remaining -= 500
	# Kapo
	elif item == 4:
		print 'Un kapo -> $200'
		remaining -= 200
	# Ferrari
	elif item == 5:
		print 'Un Ferrari -> $50.000.000'
		remaining -= 50000000
	elif item == 0:
		break
	else:
		print 'No tenemos este item'

if remaining > 0:
	print 'Alcanza y te sobran', remaining
elif remaining == 0:
	print 'Alcanza y no te sobra nada :('
else:
	print 'No te alcanza! Te faltan', -remaining