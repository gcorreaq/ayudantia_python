# Transmision de datos
from numpy import *


def numero_decimal(datos):
    exponentes = arange((len(datos) - 1), -1.0, -1.0)
    return sum(datos * (2 ** exponentes))


def bloque_valido(datos):
    return len(datos) % 4 == 0


def decodificar_bloques(datos):
    repeticiones = len(datos) / 4
    resultados = []
    i = 0

    for repeticion in range(0, repeticiones):
        resultados.append(numero_decimal(datos[i:i + 4]))
        i += 4

    if (len(datos) % 4) > 0:
        resultados.append(-1)

    return array(resultados)


####################
# Codigo de prueba #
####################
def main():
    print 'Decimal [Esperado: 9]:', numero_decimal(array([0, 1, 0, 0, 1]))
    print 'Bloque valido [Esperado: True]:', bloque_valido(
        array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))
    print 'Bloque valido [Esperado: False]:', bloque_valido(
        array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1]))

    a = array([0, 1, 0, 1])
    b = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0])
    c = array([0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1])
    print decodificar_bloques(a)
    print decodificar_bloques(b)
    print decodificar_bloques(c)


if __name__ == '__main__':
    main()
