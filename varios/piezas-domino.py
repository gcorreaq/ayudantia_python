suma = 0
contador = 0

# Se llega hasta 7 para que el ultimo
# numero de la serie sea un 6
for lado_1 in range(7):
    for lado_2 in range(lado_1, 7):
        # Para mostrar la 'pieza' actual
        print "{0} | {1}".format(lado_1, lado_2)
        # Se suman los valores
        suma += (lado_1 + lado_2)

        contador += 1

print "Total:", suma
print "Cantidad de piezas:", contador
