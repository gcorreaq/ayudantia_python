def check_item(item):
    # Sopaipillas
    if item == 1:
        price = 100
        item_description = 'Una sopaipilla'
    # Yogurt
    elif item == 2:
        price = 200
        item_description = 'Un yogurt'
    # Completo italiano
    elif item == 3:
        price = 500
        item_description = 'Un italiano'
    # Kapo
    elif item == 4:
        price = 200
        item_description = 'Un kapo'
    # Ferrari
    elif item == 5:
        price = 50000000
        item_description = 'Un Ferrari'
    else:
        price = 0

    if price > 0:
        print item_description, '->', price
    else:
        print 'No tenemos este item'

    return price


def apply_discount(count, total):
    if count < 2:
        print 'No hay descuento'
    if count == 2:
        total -= total * 0.05
        print 'Descuento del 5%'
    elif count == 3:
        total -= total * 0.1
        print 'Descuento del 10%'
    elif count == 4:
        total -= total * 0.15
        print 'Descuento del 15%'
    elif count >= 5:
        total -= total * 0.2
        print 'Descuento del 20%'

    return total
