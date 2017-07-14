# encoding: utf-8

from easy_input import get_int


def signo_zodiacal(fecha):
    # Esto es un diccionario. Cada llave tiene como valores
    # tuplas con tuplas dentro (yo dawg!)
    signos = {
        'aries': ((3, 21), (4, 20)),
        'tauro': ((4, 21), (5, 21)),
        'geminis': ((5, 22), (6, 21)),
        'cancer': ((6, 22), (7, 23)),
        'leo': ((7, 24), (8, 23)),
        'virgo': ((8, 24), (9, 23)),
        'libra': ((9, 24), (10, 23)),
        'escorpio': ((10, 24), (11, 22)),
        'sagitario': ((11, 23), (12, 21)),
        'capricornio': ((12, 22), (1, 20)),
        'acuario': ((1, 21), (2, 19)),
        'piscis': ((2, 20), (3, 20))
    }

    if len(fecha) == 3:
        _, mes, dia = fecha
        fecha = (mes, dia)

    for signo, (inicio, fin) in signos.items():
        if inicio <= fecha <= fin:
            return signo


def main():
    anno = get_int("Año: ")
    mes = get_int("Mes: ")
    dia = get_int("Dia: ")

    signo = signo_zodiacal((anno, mes, dia))

    if signo != None:
        print 'Tu signo es', signo

    # Esto es solo para mostrar el efecto que tiene capitalize()!
    # print 'Tu signo es', signo.capitalize()
    else:
        print 'Fecha invalida'


if __name__ == '__main__':
    main()
