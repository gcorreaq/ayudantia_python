# Esta solucion asume que los numeros son ingresados uno por uno
actual = 0
finished = False

while not finished:
    number = int(raw_input("Numero: "))

    if number == 1:
        print 'Usted perdio'
        finished = True
    elif actual != number:
        actual = number
        equals_count = 1
    else:
        equals_count += 1

        if equals_count == actual:
            print 'Usted gano'
            finished = True
