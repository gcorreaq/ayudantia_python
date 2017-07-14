x = float(raw_input("x: "))
precision = float(raw_input("p: "))

exponente = 1
suma = 0
iteracion = 1

while True:
    # Factorial
    factorial = 1

    for i in range(1, exponente + 1):
        factorial *= i

    # Si es iteracion par, el signo es negativo
    if iteracion % 2 == 0:
        signo = -1
    # Caso contrario, positivo
    else:
        signo = 1

    # Se calcula el termino
    termino = signo * ((x ** exponente) / factorial)
    # Se agrega a la suma
    suma += termino

    # Estos dos 'if' anidados son lo mismo que
    # if (iteracion != 1) and (abs(anterior - termino) <= precision):
    if iteracion != 1:
        if abs(anterior - termino) <= precision:
            # El break es para 'romper' el while
            # ya que se alcanzo la precision esperada
            break

    # El termino actual se guarda para ser comparado
    anterior = termino
    # El exponente aumenta de dos en dos
    exponente += 2
    # Una nueva iteracion
    iteracion += 1

print suma
