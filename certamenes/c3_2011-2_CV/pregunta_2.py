from numpy import *


def sala_mas_concurrida(arreglo):
    totales = []
    sala_actual = 1

    # Se recorreran las filas del arreglo
    for sala in arreglo:
        total_asistentes = sum(sala)
        totales.append((total_asistentes, sala_actual))
        sala_actual += 1

    # Se ordena la lista, se retorna el ultimo
    # que corresponde al con mas visitas, y
    # se retorna el numero de sala
    return sorted(totales)[-1][1]


def pelicula_mas_vista(arreglo):
    totales = []

    # Para las columnas, es mejor sacar slices
    _, cant_columnas = arreglo.shape

    # Pelicula corresponde al indice de la columna actual
    for pelicula in range(cant_columnas):
        total_asistentes = sum(arreglo[:, pelicula])
        totales.append((total_asistentes, pelicula))

    # Primero se ordena la lista
    totales.sort()

    # Se retorna el ultimo elemento, que corresponde
    # a la pelicula con mas espectadores, y de este,
    # se saca el segundo elemento de la tupla: el numero
    # de pelicula
    return totales[-1][1]


#####################
# Codigo de pruebas #
#####################

def main():
    # Las filas son las salas, y las columnas las peliculas
    # El valor en cada celda es la cantidad de asistentes
    a = array([[163, 141,  58,  95, 127,  74, 278, 203, 160, 265, 251, 213, 173,  70, 184, 268, 139, 222, 107, 275],
               [ 77, 241, 242, 183, 172,  48, 196, 232, 161,  36, 262, 220, 155, 117,  62, 215, 208, 110,  54,  61],
               [171, 132, 284,  27,  56, 230,  31, 133, 169, 238, 125,  25,  39, 250, 259, 233, 219,  97,  49, 181],
               [ 89, 108, 147, 120, 185, 210, 158, 114, 149, 211, 260,  83,  90,  52, 119,  75, 102, 236,  69,  57],
               [235, 144,  47, 151, 263, 261, 100,  93, 101, 227, 193, 180, 201,  86, 140,  85, 121,  80,  78, 106],
               [258, 116, 157, 124,  38, 189,  67, 182, 280, 270, 104,  92, 223, 237, 138,  76, 199,  94, 148,  32],
               [ 46, 214,  66, 205,  88, 249, 134, 168, 206, 221, 254, 187,  55,  45,  41, 269,  34, 122, 271, 266],
               [194,  82, 272, 198, 142,  81, 137, 165, 135,  30, 190, 252,  99, 166, 243, 212,  33, 131, 167, 152],
               [164,  96,  43, 156, 143, 179,  40,  87, 191, 111,  53, 246,  29, 283, 200, 245, 197, 123, 273, 281],
               [126, 204, 103, 253,  63, 257, 195,  98, 255, 109, 225, 159, 267, 277,  68, 162, 150, 276,  91, 128],
               [224, 216, 256,  35, 192, 248, 118,  37, 177, 174,  64, 186, 136, 274, 115, 279, 170, 175, 145, 202],
               [ 79,  44, 264, 239, 282, 207,  73, 130, 240,  59,  65,  72, 209, 231, 228,  26,  60,  28, 146, 129],
               [ 42,  50, 226, 234, 217, 113,  84, 229,  51,  71, 244, 247, 218, 176, 105, 112, 153, 178, 154, 188]])

    # La mayor cantidad de publico es 284
    # ubicado en la posicion [2, 2]
    print sala_mas_concurrida(a)
    print pelicula_mas_vista(a)


if __name__ == '__main__':
    main()
