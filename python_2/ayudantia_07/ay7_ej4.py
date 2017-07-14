# Poker
mano = []

equivalencias = {
    'j': 11,
    'q': 12,
    'k': 13
}


def es_full(mano):
    mano.sort()
    primera_carta = True
    contador = 1

    condiciones = {
        '3_seguidos': False,
        '2_seguidos': False
    }

    for carta in mano:
        numero, _ = carta

        if primera_carta:
            numero_anterior = numero
            primera_carta = False
        elif numero == numero_anterior:
            contador += 1
        else:
            if (contador == 2) and not condiciones['2_seguidos']:
                condiciones['2_seguidos'] = True
            elif (contador == 3) and not condiciones['3_seguidos']:
                condiciones['3_seguidos'] = True

            numero_anterior = numero
            contador = 1

    if (contador == 2) and not condiciones['2_seguidos']:
        condiciones['2_seguidos'] = True
    elif (contador == 3) and not condiciones['3_seguidos']:
        condiciones['3_seguidos'] = True

    return condiciones['2_seguidos'] and condiciones['3_seguidos']


def es_color(mano):
    color_referencia = None

    for carta in mano:
        _, color = carta

        if not color_referencia:
            color_referencia = color
        elif color_referencia != color:
            return False

    return True


def es_escalera(mano):
    mano.sort()
    numero_anterior = None

    for carta in mano:
        numero, _ = carta

        if not numero_anterior:
            numero_anterior = numero
        elif (numero_anterior + 1) == numero:
            numero_anterior = numero
        else:
            print numero_anterior, numero
            return False

    return True


def es_escalera_de_color(mano):
    mano.sort()
    numero_anterior = None
    color_referencia = None

    for carta in mano:
        numero, color = carta

        if not numero_anterior and not color_referencia:
            numero_anterior = numero
            color_referencia = color
        elif ((numero_anterior + 1) == numero) and (color_referencia == color):
            numero_anterior = numero
        else:
            return False

    return True


def main():
    for i in range(1, 6):
        carta = raw_input("Carta " + str(i) + ": ").lower()
        numero = carta[:len(carta) - 1]
        color = carta[-1]

        if numero in equivalencias:
            numero = equivalencias[numero]
        else:
            numero = int(numero)

        mano.append((numero, color))

    if es_escalera_de_color(mano):
        print 'Es Escalera de Color'
    elif es_escalera(mano):
        print 'Es Escalera'
    elif es_color(mano):
        print 'Es Color'
    elif es_full(mano):
        print 'Es Full'


if __name__ == '__main__':
    main()
