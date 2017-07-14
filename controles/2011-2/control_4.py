def suma_digitos(numero):
    suma = 0

    # Sumamos hasta que el numero restante sea cero
    while numero > 0:
        # Sumamos el ultimo digito de la derecha
        suma += numero % 10
        # Dividimos por 10 para eliminar el ultimo digito de la derecha
        numero /= 10

    return suma


def reducir_a_digito(numero):
    # El proceso se repite mientras el numero tenga 2 o mas digitos
    while numero = > 10:
        numero = suma_digitos(numero)

    return numero
