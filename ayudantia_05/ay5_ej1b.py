# Importamos las funciones que creamos
from easy_input import get_int


# Funciones para este programa
def divisible_por(numero, divisor):
    return numero % divisor == 0


# Inicio del programa
exit = False

while not exit:
    print '-----------------'
    print '1) Comprobar par'
    print '2) Comprobar impar'
    print '3) Comprobar divisibilidad'
    print '4) Salir'
    print ''

    option = get_int("Opcion: ")

    if option == 1:
        numero = get_int("Ingrese numero: ")

        if divisible_por(numero, 2):
            print 'Es par'
        else:
            print 'No es par'
    elif option == 2:
        numero = get_int("Ingrese numero: ")

        if not divisible_por(numero, 2):
            print 'Es impar'
        else:
            print 'No es impar'
    elif option == 3:
        numero = get_int("Ingrese numero: ")
        divisor = get_int("Ingrese divisor: ")

        if divisible_por(numero, divisor):
            print numero, 'es divisible por', divisor
        else:
            print numero, 'no es divisible por', divisor
    elif option == 4:
        exit = True
    else:
        raw_input('Opcion no valida...')

print 'Programa terminado'
