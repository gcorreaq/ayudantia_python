def canciones_pais(p):
    canciones = set()

    for pais in ciudades[p]:
        for concierto in conciertos:
            if concierto['ciudad'] in pais:
                canciones |= set(concierto['canciones'])

    # Esto dice: retorna 'canciones' si 'canciones' tiene elementos,
    # si no, retorna None
    return canciones if len(canciones) > 0 else None


def contar_exitos(n):
    for pais in ciudades:
        if len(pais) > 1:
