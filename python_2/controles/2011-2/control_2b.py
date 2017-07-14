# Control 2B

monto_inicial = int(raw_input("Monto inicial: "))
monto = monto_inicial

for i in range(1, 4):

    prediccion = int(raw_input("Prediccion dia " + str(i) + " (en %): "))
    monto += ((monto * prediccion) / 100)

    if monto >= monto_inicial:
        print 'Hay ganancia de dinero'
    else:
        print 'Hay perdida de dinero'
