from easy_input import get_int
from items_carrito import check_item, apply_discount

# Inicio del programa
money = get_int("Dinero: ")

total = 0
cuenta = 0
item = -1

while item != 0:
	item = get_int("Item (cero para terminar): ")

	if item == 0:
		break
	else:
		sub_total = check_item(item)

		if sub_total > 0:
			total += sub_total
			cuenta += 1

remaining = money - apply_discount(cuenta, total)

if remaining > 0:
	print 'Alcanza y te sobran', remaining, 'pesos'
elif remaining == 0:
	print 'Alcanza y no te sobra nada :('
else:
	print 'No te alcanza! Te faltan', abs(remaining), 'pesos'