n = int(raw_input("n: "))
cant_productos = int(raw_input("Cantidad de productos: "))

total = 0
descuento = 0.2  # El 20%
total_descuentos = 0
productos_restantes = cant_productos

for producto in range(1, cant_productos + 1):
    precio = int(raw_input("Precios producto " + str(producto) + ": "))

    # Se suma al total
    total += precio
    # Se calcula el descuento
    total_descuentos += (precio * descuento)

    # Un producto menos en la lista
    productos_restantes -= 1

    # Si quedan menos de 'n' productos, de ahora en adelante no se
    # aplica descuento
    if productos_restantes < n:
        descuento = 0
    # De lo contrario, se revisa si hay que disminuir el descuento a
    # la mitad
    else:
        if producto % n == 0:
            descuento /= 2

print 'Total:', total
print 'Descuento:', int(total_descuentos)
print 'Por pagar:', int(total - total_descuentos)
