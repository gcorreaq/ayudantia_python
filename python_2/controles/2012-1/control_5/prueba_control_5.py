import sys

temperaturas = {
    'Las Condes': (9, 26),
    'La Reina': (10, 24),
    'San Joaquin': (7, 30),
    'Las Rejas': (6, 31),
    'Vitacura': (8, 25),
    'San Miguel': (7, 29),
    'El Bosque': (-1, 34),
    'San Bernardo': (10, 12),
    'Antartica': (-15, -3), # Este es el ganador!
    'Arica': (24, 30)
}

def main():
    # Si viene un argumento, se asume que es el nombre de un archivo
    if len(sys.argv) > 1:
        import_name = sys.argv[1]
        # Se importa, omitiendo la extension del archivo
        control = __import__(import_name[:len(import_name) - 3])
    else:
        print "ERROR"
        return

    print "-- Menor diferencia de temperaturas --"
    print control.menor_minima(temperaturas)

if __name__ == '__main__':
    main()