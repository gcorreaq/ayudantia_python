# Primera alternativa de solucion

from numpy import *


# Si se encuentra la 'aguja' en el 'pajar', se retorna
# la posicion de la 'aguja'
def devolver_indice(aguja, pajar):
    indice = 0

    for elemento in pajar:
        if elemento == aguja:
            return indice

        indice += 1

    return None


def encriptar(palabra):
    palabra = palabra.upper()
    nueva_palabra = ''

    A = array(['C', 'E', 'N', 'I', 'T'])
    B = array(['P', 'O', 'L', 'A', 'R'])

    for letra in palabra:
        # Si la letra esta en el array...
        if letra in A:
            # ... se busca el indice de la letra...
            indice = devolver_indice(letra, A)
            # Y corresponde al mismo indice de la letra que tenemos
            # que reemplazar
            reemplazo = B[indice]
        elif letra in B:
            indice = devolver_indice(letra, B)
            reemplazo = A[indice]
        else:
            # No hay cambio
            reemplazo = letra

        # Se agrega el nuevo caracter
        nueva_palabra += reemplazo

    return nueva_palabra


####################
# Codigo de prueba #
####################

def main():
    print encriptar('Programacion')


if __name__ == '__main__':
    main()
