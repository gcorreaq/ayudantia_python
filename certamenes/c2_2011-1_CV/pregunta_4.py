# encoding: utf-8

# Este import es SOLO para no copiar el codigo desde el
# otro archivo
from pregunta_3 import misma_ciudad, diferencia_edad


def obtener_amigos(u):
    amigos = set()

    for amistad in amistades:
        a, b = amistad

        if u == a:
            amigos.add(b)
        elif u == b:
            amigos.add(a)

    return amigos


def recomendar_amigos(u):
    amigos = obtener_amigos(u)
    recomendacion = set()

    # Se recuperan los amigos de los amigos de 'u'
    for amigo in amigos:
        # Se aplica union entre los amigos de amigos
        # y los actualmente presentes en el conjunto
        # de recomendacion
        recomendacion |= obtener_amigos(amigo)

    # Se sacan los amigos de 'u'
    recomendacion -= amigos
    # Se saca a 'u' en caso de existir
    recomendacion -= set([u])

    # Conjunto que tendra la recomendacion final
    recomendacion_final = set()

    # Se revisa que los usuarios vivan en la misma ciudad que 'u'
    # y cumplan la condicion de diferencia de edad
    for recomendado in recomendacion:
        if misma_ciudad(recomendado, u) and diferencia_edad(recomendado, u) < 10:
            recomendacion_final.add(recomendado)

    return recomendacion_final if len(recomendacion_final) > 0 else None


####################
# Código de prueba #
####################

usuarios = {
    522514: ('Jean Dupont', 'Marseille', (1989, 11, 21)),
    587125: ('Perico Los Palotes', 'Valparaiso', (1990, 4, 12)),
    189471: ('Jan Kowalski', 'Krakow', (1994, 4, 22)),
    914210: ('Antonio Nobel', 'Valparaiso', (1983, 7, 1))
}

amistades = {
    (189471, 522514), (522514, 914210), (522514, 587125)
}

print 'Amigos >', obtener_amigos(914210)
print 'Recomendacion de amigos >', recomendar_amigos(914210)
