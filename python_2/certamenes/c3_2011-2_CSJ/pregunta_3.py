from numpy import *


def tiempo_lluvia(lluvia_por_minuto):
    cont = 0

    for lluvia_caida in lluvia_por_minuto:
        if lluvia_caida > 0:
            cont += 1

    return cont


def mayor_diferencia(lluvia_por_minuto):
    mayor = 0

    for i in range(len(lluvia_por_minuto) - 1):
        diferencia = abs(lluvia_por_minuto[i] - lluvia_por_minuto[i + 1])

        if diferencia > mayor:
            mayor = diferencia

    return mayor


def obtener_lluvia_por_hora(lluvia_por_minuto):
    lluvia_por_hora = []

    for i in range(0, len(lluvia_por_minuto), 60):
        datos_hora = lluvia_por_minuto[i:(i + 60)]
        lluvia_por_hora.append(sum(datos_hora))

    return array(lluvia_por_hora)


def llovio(historico, anno, mes, dia):
    return any(historico[anno, mes, dia] > 0)


####################
# Codigo de prueba #
####################

def generar_historico():
    return zeros((13, 12, 31, 24))


def generar_lluvia_por_minuto():
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random_integers.html#numpy.random.random_integers
    return random.random_integers(0, 10, 1440)


def main():
    historico = generar_historico()
    lluvia_por_minuto = generar_lluvia_por_minuto()

    print 'Lluvia por minuto:', lluvia_por_minuto

    print 'Cantidad de minutos con lluvia:', tiempo_lluvia(lluvia_por_minuto)
    print 'Mayor diferencia de lluvia entre dos periodos:', mayor_diferencia(lluvia_por_minuto)
    lluvia_por_hora = obtener_lluvia_por_hora(lluvia_por_minuto)
    print 'Lluvia por hora:', lluvia_por_hora

    #########################
    # Respuesta al item 'd' #
    #########################
    historico[11, 2, 22] = lluvia_por_hora

    print 'Lluvias para el 23 de Marzo del 2012:', historico[11, 2, 22]
    print 'Llovio el 23 de Marzo del 2012?:', llovio(historico, 11, 2, 22)

    # Para probar sin lluvias
    print 'Llovio el 24 de Marzo del 2012?:', llovio(historico, 11, 2, 23)


if __name__ == '__main__':
    main()
