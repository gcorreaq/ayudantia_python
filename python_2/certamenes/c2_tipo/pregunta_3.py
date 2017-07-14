def cuantos_escucharon(c):
    audiencia = 0

    for concierto in conciertos:
        if c in concierto['canciones']:
            audiencia += concierto['publico']

    return audiencia


def mismo_concierto(c1, c2):
    for concierto in conciertos:
        if (c1 in concierto['canciones']) and (c2 in concierto['canciones']):
            return True

    return False


####################
# Codigo de prueba #
####################

conciertos = [
    {
        'ciudad': 'Cairo',
        'publico': 30000,
        'canciones': [
            'If your name is main',
            'Break my heart and return',
            'Strings float around you',
        ]
    },
    {
        'ciudad': 'Moscu',
        'publico': 25000,
        'canciones': [
            'Break my heart and return',
            'Open your mind, close your file',
            'Value error'
        ]
    }
]
