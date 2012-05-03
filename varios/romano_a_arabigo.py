# numero_romano debe ser un String
def romano_a_arabigo(numero_romano):
    # Resultado de la transformacion
    resultado = 0

    # Usamos un diccionario, ya que se adapta al concepto
    # de que a cada letra le corresponde un valor
    valores = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
    }

    if len(numero_romano) > 0:
        # Con esto, siempre sumamos el primer numero
        valor_anterior = numero_romano[0]

    # Por cada letra en el numero romano (string)
    for letra in numero_romano:

        # Si la letra se encuentra en el diccionario
        if letra in valores:
            # Obtenemos su valor
            valor_actual = valores[letra]
        else:
            # Si no, la letra es invalida
            print 'Valor invalido:', letra
            return 'NaN' # NaN: Not A Number

        # Si el valor anterior es mayor o igual que el
        # valor actual, se suman
        if valor_anterior >= valor_actual:
            resultado += valor_actual
        # Si no, se restan
        else:
            # Esto equivale a:
            # resultado = (resultado - valor_anterior) + (valor_actual - valor_anterior)
            resultado += valor_actual - (2 * valor_anterior)

        # El valor actual pasa a ser el anterior, para analizar
        # la siguiente letra en el numero romano
        valor_anterior = valor_actual

    # Al terminar, retorna el numero resultante
    return resultado

# Con upper() la letra siempre sera pasada a mayuscula
numero_romano = raw_input("Numero Romano: ").upper()
print "Numero Arabigo:", romano_a_arabigo(numero_romano)