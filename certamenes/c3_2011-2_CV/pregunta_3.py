def main():
    # Diccionario con los resultados
    s = {
        'Norte': {
            'Condorito': 0,
            'Dona Tremebunda': 0
        },
        'Centro': {
            'Condorito': 0,
            'Dona Tremebunda': 0
        },
        'Sur': {
            'Condorito': 0,
            'Dona Tremebunda': 0
        }
    }

    # Se abren los archivos correspondientes
    votaciones = open('votaciones.txt')
    condorito = open('condorito.txt', 'w')
    tremebunda = open('tremebunda.txt', 'w')

    # Con esto se obtiene la cantidad de lineas
    cant_lineas = len(open('votaciones.txt').readlines())

    # Se leera cada dos lineas, lo que corresponde a un voto
    for i in range(cant_lineas / 2):
        linea = votaciones.readline().strip()

        if linea != '':
            # La linea leida es el candidato
            candidato = linea
            # El sector es la linea que sigue
            sector = votaciones.readline().strip()

            # Se formatean los datos a escribir
            datos = "{0}\n{1}\n".format(candidato, sector)

            if candidato == 'A':
                # Tremebunda
                tremebunda.write(datos)
                s[sector]['Dona Tremebunda'] += 1
            elif candidato == 'B':
                # Condorito
                condorito.write(datos)
                s[sector]['Condorito'] += 1
        else:
            return None

    condorito.close()
    tremebunda.close()
    votaciones.close()

    resultados = open('resultados.txt', 'w')

    # Se recorre el diccionario de resultados
    # Esto permite una cantidad variable de sectores y candidatos
    for sector, candidatos in s.items():
        resultados.write('Sector ' + sector + '\n')
        for candidato, votos in candidatos.items():
            resultados.write(candidato + ' ' + str(votos) + ' votos\n')

    resultados.close()


if __name__ == '__main__':
    main()
