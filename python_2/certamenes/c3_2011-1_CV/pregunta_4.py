from numpy import *


def reducir(img, f):
    filas, columnas = img.shape
    img_reducida = []

    inicio_fila = 0
    fin_fila = f

    # Como se sacan matrices de fxf, el proceso se repite
    # f veces en las filas y en las columnas, por eso se divide
    # filas/f y columnas/f
    for i in range(filas / f):
        # Donde empezara y terminara el slice
        # Este valor se reinicia para cada nuevo cambio de fila
        inicio_columna = 0
        fin_columna = f

        for j in range(columnas / f):
            # Se saca un slice de acuerdo a los limites calculados
            rebanada = img[inicio_fila:fin_fila, inicio_columna:fin_columna]
            # El promedio se saca sumando todos los elementos del array bidimensional
            # por la cantidad de elementos que tiene
            img_reducida.append(sum(rebanada) / rebanada.size)

            # Movemos los limites del slice
            inicio_columna += f
            fin_columna += f

        # Como es un cambio de fila, movemos los limites del slice
        inicio_fila += f
        fin_fila += f

    # Finalmente, la lista se transforma en array y se le aplica reshape
    # para dejarla de fxf
    img_reducida = array(img_reducida).reshape((filas / f, columnas / f))
    return img_reducida


def binarizar(img, umbral):
    filas, columnas = img.shape

    # El primer 'for' es para recorrer las filas
    for fila in range(filas):
        # El segundo, para las columnas
        for columna in range(columnas):
            if img[fila, columna] >= umbral:
                nuevo_valor = 255
            else:
                nuevo_valor = 0

            img[fila, columna] = nuevo_valor

    return img


def generar_imagen(alto, ancho):
    # Genera un array bidimensional con numeros aleatorios
    # entre 0 y 1. Despues, cada valor es multiplicado por
    # 255, asi dan numeros en el rango 0-255
    img = random.random((alto, ancho)) * 255

    # Los valores son pasados a enteros
    return img.astype(int)


####################
# Codigo de prueba #
####################

def main():
    # Se genera imagen al azar
    imagen = generar_imagen(10, 10)
    print imagen
    print reducir(imagen, 2)
    print binarizar(imagen, 190)


if __name__ == '__main__':
    main()
