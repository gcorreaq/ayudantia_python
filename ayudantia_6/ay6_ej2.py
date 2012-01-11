from easy_input import get_int, get_int_list
from math import sqrt

def media(datos):
    return float(sum(datos)) / len(datos)

def desv_estandar(datos):
    return sqrt(varianza(datos))

def varianza(datos):
    suma = 0.0
    for dato in datos:
        suma += (dato ** 2)
    
    return (suma / len(datos)) - (media(datos) ** 2)

def mediana(datos):
    # Necesitamos los datos ordenados
    # Usamos la función sorted para no perder el orden original
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)

    if n % 2 == 0:
        mediana = (datos_ordenados[n / 2] + datos_ordenados[(n / 2) + 1]) * 0.5
    else:
        mediana = datos_ordenados[((n + 1) / 2) - 1]

    return mediana

def main():
    opcion = 0

    while opcion != 5:
        print '--------------------'
        print '1) Media'
        print '2) Mediana'
        print '3) Varianza'
        print '4) Desviacion Estandar'
        print '5) Salir'

        opcion = get_int("Opcion: ")

        if opcion != 5:
            datos = get_int_list("Ingrese los datos")

            if opcion == 1:
                print 'Media:', media(datos)
            elif opcion == 2:
                print 'Mediana:', mediana(datos)
            elif opcion == 3:
                print 'Varianza:', varianza(datos)
            elif opcion == 4:
                print 'Desviacion Estandar:', desv_estandar(datos)

if __name__ == '__main__':
    main()