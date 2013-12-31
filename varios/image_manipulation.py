# -*- coding: cp1252 -*-
# AUTORES: Alex Ortega
#          Gerardo Norambuena
# FECHA: 22 de Diciembre de 2013
# VERSIÓN: 5.0

 
# Programa que realiza operaciones sobre imágenes

# CONSTANTES

# NO SE REQUIEREN CONSTANTES


############################################################################
#
#   FUNCIONES
#
############################################################################

############################################################################
#
#   IMPORTACIÓN DE FUNCIONES
#
############################################################################

# Desde el módulo PIL importo las operaciones sobre imágenes
from PIL import Image

# Importo el módulo numpy completo con sus operaciones numéricas
import numpy

############################################################################
#
# DEFINICIÓN DE FUNCIONES PROPIAS
#
############################################################################

# Función que lee una imagen, la codifica a una matriz de componentes RGB
# y la escribe en un archivo de salida .txt
# ENTRADA: String que representa el nombre y la extensión de la imagen,
#          por ejemplo "imagen.bmp"
#          String que representa el nombre y la extensión del archivo de
#          destino, por ejemplo "salida.txt"
# SALIDA:  Entrega true si el archivo fue escrito correctamente
# REQUIERE: Que la imagen exista y se encuentre en el mismo directorio del programa
#
# IMPORTANTE: NO SE REQUIERE, NI SE DEBE MODIFICAR ESTA FUNCIÓN
#
def convertirImagenAArchivo(nombreImagen, nombreDestino):
    # Se abre la imagen y se le almacena en una variable llamada imagen
    imagen = Image.open(nombreImagen)
    # Se codifica la imagen a codificación RGB para mantener el formato solicitado
    imagen = imagen.convert('RGB')
    # Se convierte la imagen a una matriz del módulo numpy
    # (No se puede operar con ella)
    matrizNumpy = numpy.array(imagen)
    # Se abre el archivo con el nombre entregado en los parámetros formales
    # en modo de escritura
    archivo = open(nombreDestino, 'w')
    # Para cada fila de la matrizNumpy
    for fila in matrizNumpy:
        # Para cada lista de 3 componentes (RGB) en la fila
        # es decir, para cada pixel en la fila
        for pixel in fila :
            # Para cada componente en el pixel
            for componente in pixel :
                # Se escribe en el archivo un espacio el valor del componente
                # se transforma el valor del componente a string para permitir
                # que python lo escriba
                archivo.write( ' ' + str(componente))
            # Se separan los pixeles de cada fila escribiendo una coma cada vez que
            # se escriben los 3 componentes del pixel
            archivo.write(',')
        # Se escribe un salto de línea cada vez que se ha recorrido una fila de la
        # matriz
        archivo.write('\n')
    # Se cierra el archivo
    archivo.close()
    # Se retorna el valor booleano True, indicando que la operación se realizó
    return True


# Función que lee un archivo .txt que representa una imagen y devuelve una matriz
# de listas.
# ENTRADA: String que representa el nombre y la extensión del archivo de
#          a leer, por ejemplo "entrada.txt"
# SALIDA:  Entrega una matriz de listas, representando una imagen
# REQUIERE: Que el archivo .txt exista y se encuentre en el mismo directorio
#           del programa
#
# IMPORTANTE: NO SE REQUIERE MODIFICAR ESTA FUNCIÓN
#
def leerArchivo(nombreEntrada):
    # Se abre el archivo con el nombre entregado como parámetro formal
    # en modo de escritura
    archivo = open(nombreEntrada,'r')
    # Se crea una matriz vacia para almacenar la salida
    matriz = []
    # Para cada linea del archivo
    for i in archivo :
        # Se genera una lista vacía que servirá para operar
        lista = []
        # Se genera una lista vacía que almacenará la fila completa de
        # la imagen
        fila = []
        # Se elimina la última coma (,) y el \n de la fila utilizando strip
        # luego se divide por las comas restantes utilizando split
        lista = i.strip(",\n").split(',')
        # Para cada pixel en la lista
        for pixel in lista :
            # Se divide el pixel por los espacios para obtener una lista con
            # las tres componentes
            aux  = pixel.split()
            # Para cada uno de los 3 elementos de aux
            # se usa un range para recorrer por índice y no por elemento
            for e in range(3) :
                # Se transforma el valor a entero
                
                aux[e] = int(aux[e])
            # Se añade aux, que es una lista de 3 elementos representando el
            # valor de rojo, verde y azul, a la fila de la matriz
            fila.append(aux)
        # Una vez que se ha recorrido la fila completa, ésta se añade a la matriz
        matriz.append(fila)
    # Se retorna la matriz
    return matriz


# Función que recibe una matriz de listas y entrega una copia exacta de la entrada
#
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos
# REQUIERE: Que la matriz exista y tenga el formato indicado
#
# IMPORTANTE: NO SE REQUIERE MODIFICAR ESTA FUNCIÓN
def copiarMatriz(matriz):
    # Se genera una matriz vacía para almacenar la copia de la matriz
    matrizResultado = []
    # Se almacena la cantidad de filas en una variable filas
    filas = len(matriz)
    # Se almacena la cantidad de  elementos por fila en una variable columnas
    columnas = len(matriz[0])
    # Para cada elemento entre 0 y la cantidad de filas
    for i in range(filas):
        # Se genera una fila vacía
        nuevaFila = []
        # Para cada elemento (Pixel) entre 0 y la cantidad de elementos por fila
        for  j in range(columnas):
            # Se obtiene la componente roja (R) de cada pixel
            rojo = matriz[i][j][0]
            # Se obtiene la componente verde (G) de cada pixel
            verde = matriz [i][j][1]
            # Se obtiene la componente azul (B) de cada pixel
            azul = matriz[i][j][2]
            # Se crea una nueva lista con las componentes rojo, verde y azul de cada pixel
            pixel = [rojo, verde, azul]
            # Se agrega el pixel a la fila de la nueva matriz
            nuevaFila.append(pixel)
        # Una vez agregados todos los pixeles de la fila original a la fila nueva,
        # se agrega la nueva fila a la matriz
        matrizResultado.append(nuevaFila)
    # Una vez agregadas todas las filas a la matriz nueva, esta se retorna
    return matrizResultado

# Función que recibe una matriz de listas y transforma a 0 todos los componentes
# de la lista que no estén representando el verde
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos,
#          donde cada lista será de la forma [0, valor, 0]
# REQUIERE: Que la matriz exista y tenga el formato indicado
#
# IMPORTANTE: NO SE REQUIERE MODIFICAR ESTA FUNCIÓN
def aislarVerde(m):
    # Se llama dentro de la función aislar verde a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola a 0
            pixel[0] = 0
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola a 2
            pixel[2] = 0
            # Se puede observar que la componente verde no se ha alterado, por lo que
            # pixel[1] = pixel[1], operación que no impactaría en el resultado
            
    # Se retorna la matriz con todos los valores rojos y azules modificados
    return matriz

# Función que recibe una matriz de listas y crea el archivo de imagen que está representando
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
#          String representando el nombre y la extensión del archivo de salida
# SALIDA:  Entrega True si el archivo fue escrito correctamente
# REQUIERE: Que la matriz exista y tenga el formato indicado
#
# IMPORTANTE: NO SE REQUIERE MODIFICAR ESTA FUNCIÓN
def convertirMatrizAImagen(matriz, nombreSalida):
    # Se convierte la matriz a un tipo de dato del módulo numpy para poder
    # realizar la conversión a imagen
    arr = numpy.array(matriz)
    # Se transforma el arr de numpy a la matriz, indicando la codificación que
    # el dato representa, el rango de los números y el formato de los números
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    # Se guarda la imagen en el archivo de salida que se indicó en los parámetros formales
    im.save(nombreSalida)
    return True


##############################################
##############################################
###                                        ###
###  FUNCIONES REQUERIDAS POR CORDINACION  ###
###                                        ###
##############################################
##############################################


#############################
##                         ##
## FUNCIONES SOBRE PIXELES ##
##                         ##
#############################

# Función que recibe una matriz de listas y crea una matriz que representa la imagen rotada en 270°
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos          
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una nueva matriz representante de la imagen rotada en 270°
# REQUIERE: Que la matriz exista y tenga el formato indicado
def rotarImagen270(m):
    # Se llama dentro de la función rotarImagen270 a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Se genera una matriz vacía para almacenar la matriz que representa la imagen rotada
    matrizRotada = []
    # Se almacena la cantidad de  elementos por fila en una variable columnas
    columnas = len(matriz[0])
    # Para cada elemento entre 0 y la cantidad de columnas
    for j in range(columnas):
        # Se genera una fila vacía para almacenar los elementos de cada columna
        nuevaFila = []
        # Para cada fila en la matriz
        for  fila in matriz:
            #Se agrega el elemento de la columna en transformación a la nueva fila
            nuevaFila.append(fila[j])
        # Una vez agregado cada j-elemento de cada fila original a la fila nueva,
        #se invierte la nueva fila para conservar la orientación de la imagen y no una imagen espectral
        nuevaFila.reverse()
        #Finalmente se agrega la nueva fila a la matriz
        matrizRotada.append(nuevaFila)
    # Una vez agregadas todas las filas a la nueva matriz, esta se retorna
    return matrizRotada


# Función que recibe una matriz de listas e invierte sus filas y columnas para representar la imagen rotada en 180°
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos          
# SALIDA:  Entrega True si el archivo fue escrito correctamente y la version invertida de filas y columnas
#          de la matriz original, la cual representa la imagen rotada en 180°
# REQUIERE: Que la matriz exista y tenga el formato indicado
def rotarImagen180(m):
    # Se llama dentro de la función rotarImagen180 a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    #Para generar la rotación en 180°, basta con realizar un doble espejo (horizontal y vertical)
    #de la imagen original
    #Se invierten las filas de la matriz
    matriz.reverse()
    #Para cada fila en la matriz
    for fila in matriz:
        #Se invierten las columnas (pixeles) de la fila respectiva.
        fila.reverse()
    # Una vez obtenido el doble espejo (o rotacion en 180°) se retorna la nueva matriz
    return matriz


# Función que recibe una matriz de listas y crea una nueva matriz que representa la rotación en 90°
# ENTRADA: Matriz especular(Imagen especular de la original)
#          esto es necesario para facilitar la transformación
#          ahorrar memoria en python, y conservar la orientación de la imagen
#          En esta matriz cada celda de la matriz es una lista de 3 elementos          
# SALIDA:  Entrega True si el archivo fue escrito correctamente
# REQUIERE: Que la matriz exista y tenga el formato indicado, y sea la imagen especular de la imagen que se desea rotar
def rotarImagen90(matrizEspecular):
    # Se llama dentro de la función rotarImagen90 a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    # Se genera una matriz vacía para almacenar la matriz que representa la imagen rotada
    matrizRotada = []
    # Se almacena la cantidad de  elementos por fila en una variable columnas
    columnas = len(matriz[0])
    # Para cada elemento entre 0 y la cantidad de columnas
    for j in range(columnas):
        # Se genera una fila vacía para almacenar los elementos de cada columna
        nuevaFila = []
        # Para cada fila en la matriz
        for  fila in matriz:
            #Se agrega el elemento de la columna en transformación a la nueva fila
            nuevaFila.append(fila[-j])
        # Una vez agregado cada j-elemento de cada fila original a la fila nueva,
        # Finalmente se agrega la nueva fila a la matriz
        matrizRotada.append(nuevaFila)
    # Una vez agregadas todas las filas a la nueva matriz, esta se retorna
    return matrizRotada

# Función que recibe una matriz de listas e invierte el orden de los pixeles en cada fila
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos       
# SALIDA:  Entrega True si el archivo fue escrito correctamente, y una versión con filas invertidas
#          de la matriz original, esta nueva matriz representa la imagen especular del original
# REQUIERE: Que la matriz exista y tenga el formato indicado
def imagenEspecular(m):
    # Se llama dentro de la función imagenEspecular a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matrizEspecular = copiarMatriz(m)
    #Para generar la imagen especular, basta con invertir los pixeles
    #en cada fila en la matriz original
    #Para cada fila en la matriz
    for fila in matriz:
        #Se invierten las columnas (pixeles) de la fila.
        fila.reverse()
    # Una vez espejada la copia de matriz original, se retorna la nueva matriz transformada
    return matrizEspecular


# Función que recibe una matriz de listas e invierte los pixeles en cada columna 
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos      
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión con columnas invertidas
#          de la matriz original, esta nueva matriz representa el reflejo horizontal del original
# REQUIERE: Que la matriz exista y tenga el formato indicado
def imagenReflejo(m):
    # Se llama dentro de la función imagenReflejo a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matrizReflejo = copiarMatriz(m)
    #Para generar la imagen reflejo(espejo horizontal), basta con invertir los pixeles
    #en cada columna de la matriz original, sin embargo
    # como la matriz es una lista, sus filas tambien pueden ser invertidas,
    # y con esto se invierte cada pixel en ellas sin necesidad de trabajarlos uno a uno
    matrizReflejo.reverse()
    #Ya reflejada la imagen, se retorna la matriz transformada

    return matrizReflejo


        
#################################
##                             ##
## FUNCIONES SOBRE COMPONENTES ##
##                             ##
#################################

# Función que recibe una matriz de listas y crea una matriz que representa la imagen en escala
# de grises, donde los componentes de pixel (R,G,B) cumplen que R = G = B.
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos         
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz donde cada pixel
#          cumple la condicion de R = G = B
# REQUIERE: Que la matriz exista y tenga el formato indicado
def escalaDeGrises(m):
    # Se llama dentro de la función escalaDeGrises a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola al mayor componente del pixel
            pixel[0] = max(pixel)
            # Se modifica el valor de la componente verde (La segunda de la lista pixel)
            # igualándola al mayor componente del pixel
            pixel[1] = max(pixel)
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola al mayor componente del pixel
            pixel[2] = max(pixel)
                        
    # Se retorna la matriz con todos los valores rojos, verdes y azules igualados

    return matriz


# Función que recibe una matriz de listas y crea una matriz que representa la imagen en negativo
#       donde los componentes de pixel (R,G,B) toman el valor opuestro en la escala de luz visible
#       es decir, para cada componente de valor i, se da un valor de 255-i
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos    
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz donde cada pixel tiene
"          los colres invertidos al original"
# REQUIERE: Que la matriz exista y tenga el formato indicado
def imagenNegativo(m):
    # Se llama dentro de la función imagenNegativo a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola al menor componente del pixel
            pixel[0] = 255- pixel[0]
            # Se modifica el valor de la componente verde (La segunda de la lista pixel)
            # igualándola al menor componente del pixel
            pixel[1] = 255- pixel[1]
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola al menor componente del pixel
            pixel[2] = 255- pixel[2]
                        
    # Se retorna la matriz con todos los valores invertidos para cada componente en todos los pixel

    return matriz


# Función que recibe una matriz de listas y crea una versión únicamente con pixeles de valor (0 0 0) ó (255 255 255)
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz, unicamente con pixeles equivalentes
#          al color blanco o negro
# REQUIERE: Que la matriz exista y tenga el formato indicado
def blancoNegro(m):
    # Se llama dentro de la función blancoNegro a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            #Si la nitides de algún componente es mayor al punto de discriminación 170
            if pixel[0] > 170 or pixel[1]>170 or pixel[2]>170:
                #El pixel es Blanco y se igualan las componentes a 255.
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola a 255
                pixel[0] = 255
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola a 255
                pixel[1] = 255
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola a 255
                pixel[2] = 255
            #En caso contrario
            else:
                # El pixel es negro y se igualan sus componentes a 0#El pixel es Blanco y se igualan las componentes a 255.
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola a 0
                pixel[0] = 0
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola a 0
                pixel[1] = 0
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola a 0
                pixel[2] = 0
    #Obtenida la transformación blanco y negro se retorna la matriz.

    return matriz

# Función que recibe una matriz de listas y crea una nueva matriz en donde cada componente de pixel, equivale al promedio
# de los componentes equivalentes en los pixeles adyacentes
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una nueva matriz que representa la imagen suavizada del original
# REQUIERE: Que la matriz exista y tenga el formato indicado
def suavizar(m):
    # Se genera una matriz vacía para almacenar la matriz de la imagen suavizada
    matrizSuavizada = []
    #Para cada fila en el total de filas (EXCLUYENDO EL BORDE)
    for i in range(len(matriz)-1):
        # Se genera una nueva fila para almacenar las filas suavizadas
        filaSuavizada = []
        # Se define una lista vacía para tomar el valor de los nuevos pixeles suavizados
        nuevoPixel = []
        # Para cada elemento (Pixel) entre 0 y la cantidad de elementos por fila (Total de columnas), EXCLUYENDO EL BORDE
        for  j in range(len(matriz[0])-1):
            #Se define un acumulador por componente, para conservar el promedio de cada componente en los pixeles del grupo
            #de pixeles adyacentes con que se trabaje respectivamente 
            suma_rojo = 0
            suma_verde = 0
            suma_azul = 0
            #Se crea una matriz de 3x3 que almacene todos los pixeles adyacentes al pixel matriz[i][j]  
            M = [[matriz[i-1][j-1], matriz[i-1][j],matriz[i-1][j+1]],[matriz[i][j-1], matriz[i][j+1]],[matriz[i+1][j-1],matriz[i+1][j],matriz[i+1][j+1]]]
            #Para cada fila en la Matriz M
            for fila in M:
                #Para cada pixel en estas filas
                for pixel in fila:
                    #Se suma el valor de la componente de cada uno de los pixeles en la matriz de adyacentes al acumulador respectivo
                    suma_rojo+= pixel[0]
                    suma_verde+= pixel[1]
                    suma_azul+= pixel[2]
            #Al terminar de sumar todos los pixeles adyacentes de un pixel, se define un nuevo pixel en la lista vacía
            #Este nuevo Pixel contiene las suma de las componentes de cada pixel adyacente al original
            nuevoPixel = [suma_rojo, suma_verde, suma_azul]
            #Para cada una de estas componentes del nuevo Pixel
            for componente in nuevoPixel:
                #Se obtiene el promedio de las componentes adyacentes, dividiendo la suma de sus valores por el total de adyacentes
                #al pixel original
                componente /= 8

            #Una vez obtenido el pixel suavizado, este se agrega a la nueva fila suavizada        
            filaSuavizada.append(nuevoPixel)
        #Al terminar de recorrer una fila completa, la fila suavizada que se ha generado se agrega a la nueva matriz suavizada
        matrizSuavizada.append(filaSuavizada)
    #Finalmente se retorna la matriz suavizada

    return matrizSuavizada


##################################
##                              ##
## FUNCIONES DE CREACION PROPIA ##
##                              ##
##################################

# Función que recibe una matriz de listas y crea un mosaico de tablero de dama con un ancho elegido por el usuario
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz original en la cual se han igualado a negro
#          áreas geométricas específicas en la matriz
# REQUIERE: Que la matriz exista y tenga el formato indicado
def tableroAjedrez(m):
    # Se llama dentro de la función tableroAjedrez a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    #Se define el ancho de los cuadros de mosaico a gusto del usuario
    ancho_cuadrado = input("Ingrese el ancho del mosaico que desea:")
    #Se define un "Switch" para activar o desactivar el pintado
    pintar = False
    for fila in range(len(matriz)):
        # Se cambia el switch de pintado solo en los extremos del cuadrado para el mosaico
        if fila % ancho_cuadrado == 0:
            pintar = not pintar
            
        # Se almacena el estado inicial de la fila, ya que
        # define el comportamiento de los píxeles de toda la fila.
        # Si no almacenamos el estado inicial, la situación de la siguiente fila dependerá del
        # estado del último píxel en la fila precedente(y esto genera patrones muy raros!)
        estado_inicial = pintar
 
        for pixel in range(len(matriz[fila])):
            # Se cambia el switch de pintado solo en los extremos del cuadrado para el mosaico
            if pixel % ancho_cuadrado == 0:
                pintar = not pintar
 
            if pintar:
                matriz[fila][pixel][0] = 0
                matriz[fila][pixel][1] = 0
                matriz[fila][pixel][2] = 0
 
        pintar = estado_inicial

    return matriz


# Función que recibe una matriz de listas y crea un mosaico de tablero de dama con un ancho elegido por el usuario
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz original en la cual se han igualado a negro
#          áreas geométricas específicas en la matriz
# REQUIERE: Que la matriz exista y tenga el formato indicado
def mosaicoSepia(m):
    # Se llama dentro de la función mosaicoTablero a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    #Se define el ancho de los cuadros de mosaico a gusto del usuario
    ancho_cuadrado = input("Ingrese el ancho del mosaico que desea:")
    intensidad = input("Ingrese la intensidad del mosaico sepia:")
    
    #Se define un "Switch" para activar o desactivar el pintado
    pintar = False
    for i in range(len(matriz)):
        # Se cambia el switch de pintado solo en los extremos del cuadrado para el mosaico
        if i % ancho_cuadrado == 0:
            pintar = not pintar
            
        # Se almacena el estado inicial de la fila, ya que
        # define el comportamiento de los píxeles de toda la fila.
        # Si no almacenamos el estado inicial, la situación de la siguiente fila dependerá del
        # estado del último píxel en la fila precedente(y esto genera patrones muy raros!)
        estado_inicial = pintar
 
        for j in range(len(matriz[0])):
            # Se cambia el switch de pintado solo en los extremos del cuadrado para el mosaico
            if j % ancho_cuadrado == 0:
                pintar = not pintar
 
            if pintar:
                tonalidad = ( matriz[i][j][0] + matriz[i][j][1] +  matriz[i][j][2])/len(matriz[i][j])
                matriz[i][j][0] += tonalidad + intensidad*2
                matriz[i][j][1] += tonalidad + intensidad
                matriz[i][j][2] -= tonalidad + intensidad

            else:
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola al mayor componente del pixel
                matriz[i][j][0] = max( matriz[i][j])
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola al mayor componente del pixel
                matriz[i][j][1] = max( matriz[i][j])
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola al mayor componente del pixel
                matriz[i][j][2] = max(matriz[i][j])
 
        pintar = estado_inicial
    return matriz

# Función que recibe una matriz de listas y crea una versión de la matriz con valores maximizados o anulados de cada
# componente en los pixeles
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Una versión de la matriz, que representa la imagen con tonos vivos aumentados, y tonos suaves eliminados
# REQUIERE: Que la matriz exista y tenga el formato indicado
def colorVivo(m):
    # Se llama dentro de la función colorVivo a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz:
        # Para cada pixel en la fila
        for pixel in fila:
            for componente in pixel:
                if componente >150:
                    componente = 255
                else:
                    componente = 0

    return matriz                


# Función que recibe una matriz de listas y crea una versión de la matriz con altos valores de rojo, sutil aumento
# de la componente verde, y una disminución de la componente azul en cada pixel de la matriz
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz, que representa la imagen con
#          efecto sepia (Instagram)
# REQUIERE: Que la matriz exista y tenga el formato indicado
def efectoInstagram(m):
    # Se llama dentro de la función efectoInstagram a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    intensidad = input("Ingrese un valor entre 0 y 100 para definir la intensidad del efecto sepia:") 
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            tonalidad = (pixel[0] +pixel[1] + pixel[2])/len(pixel)
            
            #El pixel es Blanco y se igualan las componentes a 255.
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola a 255
            pixel[0] = tonalidad + intensidad*2
            # Se modifica el valor de la componente verde (La segunda de la lista pixel)
            # igualándola a 255
            pixel[1] = tonalidad + intensidad
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola a 255
            pixel[2] = tonalidad - intensidad
            #En caso contrario
            # El pixel es negro y se igualan sus componentes a 0#El pixel es Blanco y se igualan las componentes a 255.
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola a 0
            if pixel[0] > 255:
                pixel[0] = 255
            if pixel[1] > 255:
                pixel[1] = 255
            if pixel[2] > 255:
                pixel[2] = 255
                
    #Obtenida la transformación sepia se retorna la matriz.

    return matriz



# Función que recibe una matriz de listas y crea una versión de la matriz con modificaciones en los pixeles segun
# una combinación de criterios
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Entrega True si el archivo fue escrito correctamente y una versión de la matriz que representa a la nueva imagen
#          que combina los efectos sepia para un rango intermedio de intensidad de colores, y blanco y negro para valores extremos.
# REQUIERE: Que la matriz exista y tenga el formato indicado
def resplandor(m):
    # Se llama dentro de la función resplandor a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    intensidad = input("Ingrese un valor entre 0 y 100 para definir la intensidad del efecto resplandor:") 
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            #Si la nitides de algún componente es mayor al punto de discriminación 200
            if pixel[0] > 200 or pixel[1] > 200 or pixel[2] > 200:
                #El pixel es Blanco y se igualan las componentes a 255.
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola a 255
                pixel[0] = 255
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola a 255
                pixel[1] = 255
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola a 255
                pixel[2] = 255
            #Si la nitides de algún componente es menor al punto de discriminación 60
            elif pixel[0] < 60 or pixel[1] < 60 or pixel[2] < 60:
                # El pixel es negro y se igualan sus componentes a 0#El pixel es Blanco y se igualan las componentes a 255.
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola a 0
                pixel[0] = 0
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola a 0
                pixel[1] = 0
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola a 0
                pixel[2] = 0 
            #En otro caso
            else:
                tonalidad = (pixel[0] +pixel[1] + pixel[2])/len(pixel)
                # Se modifica el valor de la componente roja (La primera de la lista pixel)
                # igualándola a la tonalidad sepia
                pixel[0] = tonalidad + intensidad*2
                # Se modifica el valor de la componente verde (La segunda de la lista pixel)
                # igualándola a sepia
                pixel[1] = tonalidad + intensidad
                # Se modifica el valor de la componente azul (La tercera de la lista pixel)
                # igualándola a sepia
                pixel[2] = tonalidad - intensidad
                if pixel[0] > 255:
                    pixel[0] = 255
                if pixel[1] > 255:
                    pixel[1] = 255
                if pixel[2] > 255:
                    pixel[2] = 255
                
    #Obtenida la transformación sepia se retorna la matriz.

    return matriz

# Función que recibe una matriz de listas y transforma a 0 todos los componentes
# de la lista que no estén representando el rojo
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos,
#          donde cada lista será de la forma [valor, 0, 0]
# REQUIERE: Que la matriz exista y tenga el formato indicado
def aislarRojo(m):
    # Se llama dentro de la función aislarRojo a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente verde (La segunda de la lista pixel)
            # igualándola a 0
            pixel[1] = 0
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola a 2
            pixel[2] = 0
            # Se puede observar que la componente roja no se ha alterado, por lo que
            # pixel[0] = pixel[0], operación que no impactaría en el resultado
            
    # Se retorna la matriz con todos los valores verde y azules modificados

    return matriz

# Función que recibe una matriz de listas y transforma a 0 todos los componentes
# de la lista que no estén representando el Azul
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos,
#          donde cada lista será de la forma [0, 0, valor]
# REQUIERE: Que la matriz exista y tenga el formato indicado
def aislarAzul(m):
    # Se llama dentro de la función aislarAzul a la función
    # copiaMatriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiarMatriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola a 0
            pixel[0] = 0
            # Se modifica el valor de la componente verde (La segunda de la lista pixel)
            # igualándola a 0
            pixel[1] = 0
            # Se puede observar que la componente azul no se ha alterado, por lo que
            # pixel[2] = pixel[2], operación que no impactaría en el resultado
            
    # Se retorna la matriz con todos los valores rojos y azules modificados

    return matriz

    
#######################
##                   ##
## FUNCIONES DE MENU ##
##                   ##
#######################

# Función de que organiza las elecciones del usuario segun las selecciones de los diferentes menú
# ENTRADA: eleccion previa en menu principal      
# SALIDA:  diccionario que almacena las acciones elegidas en formato {menu : opcion}
# REQUIERE: Que las opciones y menú seleccionados existan
def eleccionUsuario(menu):
    #Se define un diccionario vacío
    diccionario_elecciones={}
    #Se vincula el menú de entrada con la funcion que le corresponde, y se llama a la funcion
    #para que el usuario elija una opcion
    if menu == "rotacion":
        opcion = menuRotar()
        diccionario_elecciones[menu] = opcion
        
    elif menu == "espejo":
        opcion = menuEspejos()
        diccionario_elecciones[menu] = opcion
        
    elif menu == "filtro":
        opcion = menuFiltros()
        diccionario_elecciones[menu] = opcion
        
    elif menu == "ayuda":
        opcion = menuAyuda()
        diccionario_elecciones[menu] = opcion
        
    elif menu == "salir":
        opcion = menuSalida()
        diccionario_elecciones[menu] = opcion

        
    #Una vez tomadas las decisiones del usuario, se retorna el par (menú:opcion) en un diccionario    
    return  diccionario_elecciones


   
    

# Función de menú principal que permite al usuario decidir sobre que tipo de uso dar al programa 
# ENTRADA: No requiere        
# SALIDA:  Función que representa la opción escogida por el usuario
# REQUIERE: Sin requisitos
def menu():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "================USACH EFFECTS====================="
    print
    print " ¿ Qué deseas hacer a continuación ? "
    print " 1. Rotar "
    print " 2. Generar espejo "
    print " 3. Aplicar filtros "
    print
    print " 4. Ayuda "
    print " 5. Salir "
    print
    #Se solicita al usuario que elija una opción
    eleccion_menu = raw_input( " Ingresa la opción que deseas: " )

    #Según su elección se define la variable opcion
    if eleccion_menu == "1":
        opcion = "rotacion"

    elif eleccion_menu == "2":
        opcion = "espejo"

    elif eleccion_menu == "3":
        opcion = "filtro"


    elif eleccion_menu == "4":
        opcion = "ayuda"

    elif eleccion_menu == "5":
        opcion = "salir"

    #Si el valor ingresado no se encuentra en la lista de opciones
    #se solicita elegir nuevamente una opción válida
    else:
        #Mensaje de aviso en pantalla para solicitar una opcion válida
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        #Se llama recursivamente a la misma función para utilizar una opcion valida
        opcion = menu()
    #Se retorna la variable opción que representa la eleccion del usuario
    return opcion



# Función que permite elegir tipo de rotación que se desea realizar 
# ENTRADA: No requiere       
# SALIDA:  Función de rotación que representa la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú principal
def menuRotar():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "================ROTACIONES====================="
    print
    print " 1.  90 grados hacia la derecha"
    print " 2.  90 grados hacia la izquierda"
    print " 3. 180 grados "
    print
    print " 0. Regresar al menú principal "
    print
    #Se solicita al usuario que elija una opción
    rotacion = raw_input( " Ingrese la opcion que desea: " )
    #Según su elección se define la variable rotar
    if rotacion == "1":
         rotar = "90D"

    elif rotacion == "2":
        rotar = "90I"

    elif rotacion == "3":
        rotar = "180"

    elif rotacion == "0":
        rotar = 0
    #Si el valor ingresado no se encuentra en la lista de opciones
    #se solicita elegir nuevamente una opción válida
    else:
        #Mensaje de aviso en pantalla para solicitar una opcion válida
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        #Se llama recursivamente a la misma función para utilizar una opcion valida
        rotar = menuRotar()
    #Se retorna la variable rotar que representa la eleccion del usuario
    return rotar
    

# Función de menú que permite al usuario decidir sobre que tipo de espejo generar para su imagen 
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú principal
def menuEspejos():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "================Imagen Espejo====================="
    print
    print " 1. Imagen especular ó espejo vertical"
    print " 2. Imagen reflejada ó espejo Horizontal"
    print
    print " 0. Regresar al menú principal "
    print
    #Se solicita al usuario que elija una opción
    espejo = raw_input( " Ingrese la opcion que desea: " )
    #Según su elección se define la variable espejar
    if espejo == "1":
         espejar = "especular"

    elif espejo == "2":
        espejar = "reflejo"

    elif menu == "0":
        espejar = 0
    #Si el valor ingresado no se encuentra en la lista de opciones
    #se solicita elegir nuevamente una opción válida
    else:
        #Mensaje de aviso en pantalla para solicitar una opcion válida
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        #Se llama recursivamente a la misma función para utilizar una opcion valida
        espejar = menuEspejos()
    #Se retorna la variable espejar que representa la eleccion del usuario
    return espejar
    

# Función de menú que permite al usuario decidir sobre que tipo de filtro aplicar a su imagen 
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú principal
def menuFiltros():
    #Se despliega un menú en pantalla con las opciones a elegir
    print "================Filtros de Imagen====================="
    print
    print " 1. Aislar Color "
    print " 2. Escala de Grises "
    print " 3. Blanco y Negro "
    print " 4. Imagen en Negativo"
    print " 5. Resplandor "
    print " 6. Suavizar "
    print " 7. Color Vivo " 
    print " 8. Mosaico Ajedrez "
    print " 9. Mosaico Sepia"
    print
    print " 0. Volver al menú principal"
    print
    #Se solicita al usuario que elija una opción
    filtro = raw_input( " Ingresa la opción que deseas: " )
    #Según su elección se define la variable filtrar
    #En el caso de aislar color, existen 3 alternativas, por lo que se ingresa a un submenu
    if filtro == "1":
        #Se activa un switch para mantenerse dentro del sub-menu hasta obtener una elección válida
        bucle = True
        #Se despliega un sub-menú en pantalla con las opciones de aislado disponibles
        print " 1. Aislar Rojo"
        print " 2. Aislar Verde"
        print " 3. Aislar Azul"
        #Mientras el switch está encendido (TRUE)
        while bucle == True:
            #Se solicita al usuario que elija un color
            aislado = raw_input(" Ingrese el color que desea aislar en la imagen: ")
            #Según su elección se define el aislado que se aplicará
            #Si se elije una opción válida, el switch se apaga (not bucle = FALSE)
            if aislado == "1":
                filtrar = "rojo"
                bucle = not bucle
            
            elif aislado == "2":
                filtrar = "verde"
                bucle = not bucle

            elif aislado == "3":
                filtrar= "azul"
                bucle = not bucle
            #En caso contrario
            else:
                #Se informa de la opción invalida y el ciclo se repite
                print " La opción ingresada no es válida, porfavor intenta nuevamente "
    #En los demás casos define la variable filtrar de manera normal
    elif filtro == "2":
        filtrar = "gris"

    elif filtro == "3":
        filtrar = "blanco_negro" 

    elif filtro == "4":
        filtrar = "negativo"

    elif filtro == "5":
        filtrar = "resplandor"

    elif filtro == "6":
        filtrar = "suavizado"

    elif filtro == "7":
        filtrar = "color"

    elif filtro == "8":
        filtrar = "ajedrez"

    elif filtro == "9":
        filtrar = "mosaico"

    elif  filtro == "0":
        filtrar = 0
    #En caso de no elegir un filtro valido       
    else:

        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        filtrar = menuFiltros()
    #Una vez elegido un filtro, se retorna la variable filtrar que representa la elección del usuario
    return filtrar


# Función de menú que permite al usuario obtener información sobre las posibilidades del programa
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú principal
def menuAyuda():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "================Menú de Ayuda====================="
    print
    print " Con este menú obtentras información sobre: "
    print
    print " 1. Como ingresar una imagen "
    print " 2. Tipos de transformaciones "
    print
    print " 3. Volver al menú principal "
    print " 4. Salir del programa "
    #Se solicita al usuario que elija una opción
    ayuda = raw_input( " Ingresa la opción que deseas: " )
    #Según su elección se despliega en ventana la informacion solicitada
    if ayuda == "1":
        
        print "================Como ingresar una imagen====================="
        print
        print "Requisitos de imagen y equipo"
        print
        print "- La imagen debe estar en formato JPG, PNG ó BMP. "
        print
        print "- Si tu imagen tiene dimensiones superiores a 300x300 pixeles, asegura de que tu equipo"
        print "   posee suficiente memoria ram disponible "
        print "   NOTA:(el proceso de algunos filtrospuede tardar varios segundos) "
        print
        print "Para ingresar tu imagen sigue los siguientes pasos:"
        print
        print "1. Agrega tu imagen a la misma carpeta donde se encuentra instalado UsachEffects"
        print
        print "2. En el menú de bienvenida, te será solicitado el nombre de tu imagen"
        print "   Asegurate de ingresar el nombre de tu imagen correctamente,"
        print "   incluyendo su extensión de formato. Por ejemplo: imagen.jpg"
        print 
        print "3. Te será solicitado el nombre del archivo .txt que conservará la información numérica"
        print "   de tu imagen. Se debe incluir la extensión.txt"
        print
        print "4. Ya en el menú principal, solo sigue los pasos y elije la transformación que prefieras"
        print
        print "5. Disfruta transformando tus imagenes favoritas!! "
        #Se define la variable ayudar, que da acceso a al siguiente sub-menu, donde el usuario elegirá
        #como proseguir
        ayudar = 1 

    elif ayuda == "2":
        print "================Tipos de Transformaciones====================="
        print
        print "UsachEffects cuenta con diferentes tipos de transformación para tus imagenes:"
        print
        print " 1. EFECTOS DE ROTACION "
        print
        print "    Las rotaciones son transformaciones de pixeles, es decir, la calidad, nitidez, o colores"
        print "    de tu imagen no se verán afectados."
        print "    Este tipo de transformación sólo reordena la orientación de tu imagen"
        print "    Encontraras la posibilidad de realizar 3 tipos de rotaciones en UsachEffects"
        print 
        print " 2. EFECTOS DE ESPEJO"
        print
        print "    Al igual que las rotaciones, los efectos de espejo generan transformaciones de pixeles,"
        print "    es decir, la calidad, nitidez, o colores de tu imagen no se verán afectados."
        print "    Este tipo de transformación sólo invertirá el sentido de apreciación de tu imagen"
        print "    Encontraras la posibilidad de realizar 2 tipos de espejos en UsachEffects"
        print
        print " 3. EFECTOS DE FILTROS "
        print
        print "    Los filtros a diferencia de las rotaciones y espejos, son transformaciones de componentes,"
        print "    es decir, alterarán los colores ó nitidez de tus imagenes añadiendo efectos increibles. "
        print "    Este tipo de transformación es muy diversa!! y cambiará radicalmente el aspecto de tu imagen,"
        print "    sin embargo, UsachEffect siempre guardará una copia original de tu imagen."
        print "    Encontraras la posibilidad de realizar NUEVE!! tipos de efectos por filtro en UsachEffects, "
        print "    algunos de ellos incluso personalizables, por lo que tus posibilidades son infinitas!! "
        print
        #Se define la variable ayudar, que da acceso a al siguiente sub-menu, donde el usuario
        #puede obtener informacion más específica sobre las transformaciones de Usach Effects
        ayudar = 3
    #Se consideran los casos donde el usuario pueda elegir regresar
    #a un menú previo o salir del programa
    elif ayuda == "3":
        ayudar = 0

    elif ayuda == "4":
        ayudar = menuSalida()
    #En caso contrario se inciste recursivamente para buscar una opción válida
    else:
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        ayudar = menuAyuda()
    #Se retorna la elección del usuario en la variable ayudar
    return ayudar

# Función de menú que permite al usuario regresar a un menú anterior 
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú de ayuda
def menuRetorno1():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "=============================="
    print
    print "1. Regresar al menú de ayuda"
    print "2. Regresar al menú principal"
    #Se solicita al usuario que elija una opción
    opcion = raw_input("¿ Qué desea hacer?: ")
    #Según la opción elegida se retorna a otro menú
    if opcion == "1":
        retornar = menuAyuda()

    elif opcion == "2":
        retornar = 0
    #En caso contrario se inciste recursivamente para buscar una opción válida
    else:
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        retornar = menuRetorno1()
    #Se retorna la elección del usuario en la variable retornar
    return retornar

# Función de menú que permite al usuario regresar a un menú anterior 
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú de tipos de transformación
def menuRetorno2():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "============================================"
    print
    print "1. Ayuda sobre otro tipo de Transformación" 
    print "2. Regresar al menú de ayuda"
    print "3. Regresar al menú principal"
    #Se solicita al usuario que elija una opción
    opcion = raw_input("¿Qué desea hacer?: ")
    #Según la opción elegida se retorna a otro menú
    if opcion == "1":
        retornar = menuTiposDeTransformacion()

    elif opcion == "2":
        retornar = menuAyuda()

    elif opcion == "3":
        retornar = 0
    #En caso contrario se inciste recursivamente para buscar una opción válida
    else:
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        retornar = menuRetorno2()
    #Se retorna la elección del usuario en la variable retornar
    return retornar

# Función de menú que permite al usuario acceder a información más específica sobre los tipos de transformacion
# de UsachEffects, también permite regresar a un menú anterior
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú de ayuda
def menuTiposDeTransformacion():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "===========Ayuda Tipos de Transformaciones=========="
    print
    print "1. Más sobre Rotaciones"
    print "2. Más sobre Espejos"
    print "3. Más sobre Filtros"
    print
    print "4. Volver al menú de ayuda"
    print "5. Volver al menú principal"
    #Se solicita al usuario que elija una opción
    opcion = raw_input("¿ Qué desea hacer?: ")
    
    #Según la opción elegida se retorna a otro menú
    if opcion == "1":
        print
        print "================Rotaciones====================="
        print
        print " 1. EFECTOS DE ROTACION "
        print
        print "    Las rotaciones son transformaciones de pixeles, es decir, la calidad, nitidez, o colores"
        print "    de tu imagen no se verán afectados."
        print "    Este tipo de transformación sólo reordena la orientación de tu imagen"
        print "    Encontraras la posibilidad de realizar 3 tipos de rotaciones en UsachEffects"
        print
        print "    Estos son:"
        print "1.1 Rotaciones en 90°:"
        print   
        print "    Las rotaciones en 90° generan una imagen perpendicular a la original"
        print "    Podrás realizar rotaciones en 90° en ambos sentidos de giro"
        print "    La rotación hacia la derecha girará tu imagen en sentido horario"
        print "    La rotación hacia la izquierda girará tu imagen en sentido anti-horario"
        print 
        print "1.2 Rotación en 180°:"
        print "    La rotación en 180° genera una imagen invertida en ambos ejes"
        print "    También se puede interpretar como una doble rotación de 90°"
        print
        #Se define el retorno a un sub-menu para que el usuario decida como continuar
        retornar = menuRetorno2()

    elif opcion == "2":
        print
        print "================Espejos====================="
        print
        print " 2. EFECTOS DE ESPEJO"
        print
        print "    Al igual que las rotaciones, los efectos de espejo generan transformaciones de pixeles,"
        print "    es decir, la calidad, nitidez, o colores de tu imagen no se verán afectados."
        print "    Este tipo de transformación sólo invertirá el sentido de apreciación de tu imagen"
        print "    Encontraras la posibilidad de realizar 2 tipos de espejos en UsachEffects"
        print
        print "2.1 Espejo vertical o imagen especular"
        print "    El espejo vertical genera una imagen especular que es identica a la original pero invertida,"
        print "    es un flip vertical, tal y como cuando te observas en el espejo "
        print
        print "2.2 Espejo horizontal o imagen reflejo"
        print "    El espejo horizontal genera una imagen especular que es identica a la original pero invertida,"
        print "    es un flip horizontal, tal y como cuando te reflejas en el agua "
        print
        #Se define el retorno a un sub-menu para que el usuario decida como continuar
        retornar = menuRetorno2()

    elif opcion == "3":
        print
        print "================Filtros====================="
        print
        print " 3. EFECTOS DE FILTROS "
        print
        print "    Los filtros a diferencia de las rotaciones y espejos, son transformaciones de componentes,"
        print "    es decir, alterarán los colores ó nitidez de tus imagenes añadiendo efectos increibles. "
        print "    Este tipo de transformación es muy diversa!! y cambiará radicalmente el aspecto de tu imagen,"
        print "    sin embargo, UsachEffect siempre guardará una copia original de tu imagen."
        print "    Encontraras la posibilidad de realizar NUEVE!! tipos de efectos por filtro en UsachEffects, "
        print "    algunos de ellos incluso personalizables, por lo que tus posibilidades son infinitas!! "
        print
        print "3.1 Aislar Color"
        print "    Aislar color, presenta una versión de la imagen en tonalidades de un único color"
        print "    que es elegido por el usuario. Los alisados disponibles en esta versión son:"
        print "    Azul, Verde y Rojo"
        print
        print "3.2 Escala de Grises"
        print "    La escala de grises transforma la imagen extrayendo todo color, y presentandola"
        print "    solo en tonalidades de gris. El usuario puede elegir la intensidad del efecto"
        print
        print "3.3 Blanco y Negro"
        print "    Este filtro extrae todo el color de la iamgen, y entrega una artistica version solo en blanco y negro puros"
        print
        print "3.4 Imagen en Negativo"
        print "    Como lo sugiere el nombre, este filtro entrega el negativo de la imagen, es decir, con sus colores"
        print "    invertidos en la escala de luz visible"
        print
        print "3.5 Resplandor"
        print "    Este efecto genera la sensación de intensa luz y alto contraste con las sombras en la imagen"
        print "    Es una suerte de combinación entre los filtros de Sepia, y el alto contraste de Blanco y negro"
        print
        print "3.6 Suavizar"
        print "    El suavizado es un desenfoque de la imagen original, genera el efecto de sueño"
        print
        print "3.7 Color Vivo"
        print "    El filtro de color vivo intensifica significativamente las tonalidades básicas"
        print "    generando un efecto atractivo y artistico"
        print
        print "3.8 Tablero de Ajedrez"
        print "    Este filtro superpone un cuadriculado negro en la imagen, dejando intactos los espacios intermedios,"
        print "    simulando un tablero de ajedréz"
        print "    Las dimensiones del cuadriculado, son elegidas por el usuario"
        print
        print "3.9 Mosaico"
        print "    Este filtro es similar al tablero de ajedrez, sin embargo, modifica todos los colores de la imagen,"
        print "    intercalando un efecto de decolorado (tonos grises), con un efecto sepia"
        print "    Tanto las dimenciones del cuadriculado como la intensidad del efecto sepia, son elegidas por el usuario"
        print
        #Se define el retorno a un sub-menu para que el usuario decida como continuar
        retornar = menuRetorno2()

    elif opcion == "4":
        retornar = menuRetorno1()

    elif opcion == "5":
        retornar = 0
    #En caso contrario se inciste recursivamente para buscar una opción válida
    else:
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        retornar = menuTiposDeTransformacion()
    #Se retorna la elección del usuario en la variable retornar
    return retornar
        
        
    
# Función de menú que permite al usuario salir del programa o regresar al menú principal 
# ENTRADA: No requiere        
# SALIDA:  Función representada por la opción elegida por el usuario
# REQUIERE: Ser solicitada por el usuario desde el menú principal
def menuSalida():
    #Se despliega un menú en pantalla con las opciones a elegir
    print
    print "=================SALIDA======================="
    print
    print " ¿Esta seguro que desea salir de la aplicación?"
    print " 1. No, volver al menú principal"
    print " 2. Sí, Deseo salir"
    #Se solicita al usuario que elija una opción
    salida = raw_input(" Ingrese su opción ")
    #Se define la variable salir segun su elección
    if salida == "1":
        salir = 0
    elif salida == "2":
        salir = 1
    #En caso de ingresar un valor inválido, se inciste recursivamente
    else:
        print " La opción ingresada no es válida, porfavor intenta nuevamente "
        salir = menuSalida()
    #Se retorna la variable salir que representa la eleccion del usuario
    return salir
  
##############################################################################################
#
#
#       BLOQUE PRINCIPAL
#
#
##############################################################################################


#
# ENTRADA
#

##Se despliega un menú en pantalla con Bienvenida
print "*************************************************************"
print "=====================USACH EFFECTS==========================="
print "*************************************************************"
print
print "------------------------Bienvenido---------------------------"
print
print
#Se solicita el nombre y formato de la imagen con la que se trabajará
print "Ingrese la imagen a procesar,",
nombreEntrada = raw_input("por ejemplo, imagen.bmp: ")
#Se solicita el nombre y formato del archivo que guardará la matriz numérica
#que representa a la imagen original
print "Ingrese el nombre del archivo de destino,",
nombreSalida = raw_input("por ejemplo, salida.txt ")

#Se define la variable que convertira la imagen en un archivo de datos
archivoExitoso=convertirImagenAArchivo(nombreEntrada, nombreSalida)
#Si el archivo se crea
if archivoExitoso:
    #Se muestra mensaje en pantalla para confirmar el nuevo archivo 
    print "El archivo ", nombreSalida, " se ha creado exitosamente"
    #Se define la variable que transformará el archivo de texto, en una matriz operable
    matriz = leerArchivo(nombreSalida)

#
# PROCESAMIENTO
#

#Se define un switch de salida, OFF
salida = False
#Mientras el switch esté en OFF
while salida == False:
    #Se muestra el menú principal
    iniciar = menu()
    #Se define el diccionario de procesos invocando la funcion con las elecciones del usuario
    proceso = eleccionUsuario(iniciar)
    #Se define la variable que asegurará la creación de la copia en cada uso del programa
    copiaOriginal= copiarMatriz(matriz)

    #Si el usuario ha elejido la opción salir
    if proceso.has_key("salir"):
        #No se generan copias de imagen para las elecciónes de este menú
        copia = "nula"
        #Si el usuario ha confirmado su salida
        if proceso["salir"] == 1:
            #Se muestra mensaje de despedida en pantalla
            print "Hasta pronto"
            #Se activa el switch de salida y se finaliza el bucle
            salida = True
            
    #En caso contrario
    else:
        #Para cada tipo de accion elegida por el usuario
        for key in proceso.keys():
            #Se ha configurado cada menú para asignar el valor 0 a la llave respectiva
            #Si el usuario decide desde cualquier sitio regresar al menú principal
            #Si es así:
            if proceso[key] == 0:
                menu()

            #Para todos los otros casos, en que se eligen transformaciones
            #Se asigna un valor (no necesariamente numérico) a la llave del proceso respectivo
            #por ejemplo: proceso de rotacion, en 90°
            #             genera el elemento de diccionario { "rotacion" : "90I" }
            #Se define tambien el tipo de copia que debe realizarse modificando la imagen original
            #segun lo solicitado por el usuario, invocando a la función apropiada para dicha
            #transformación
            if key == "rotacion":
                if proceso[key] == "90D":
                    copia = rotarImagen270(matriz)
                    
                if proceso[key] == "90I":
                    copia = rotarImagen90(matriz)
                    
                if proceso[key] == "180":
                    copia = rotarImagen180(matriz)

            if key == "espejo":
                if proceso[key] == "especular":
                    copia = imagenEspecular(matriz)
                    
                if proceso[key] == "reflejo":
                    copia = imagenReflejo(matriz)
                    
            if key == "filtro":
                if proceso[key] == "rojo":
                    copia = aislarRojo(matriz)
                    
                if proceso[key] == "verde":
                    copia = aislarVerde(matriz)
                    
                if proceso[key] == "azul":
                    copia = aislarAzul(matriz)
                    
                if proceso[key] == "gris":
                    copia = escalaDeGrises(matriz)
                    
                if proceso[key] == "blanco_negro":
                    copia = blancoNegro(matriz)
                    
                if proceso[key] == "negativo":
                    copia = imagenNegativo(matriz)
                    
                if proceso[key] == "resplandor":
                    copia = resplandor(matriz)
                    
                if proceso[key] == "suavizado":
                    copia = suavizar(matriz)

                if proceso[key] == "color":
                    copia = colorVivo(matriz)

                if proceso[key] == "ajedrez":
                    copia = tableroAjedrez(matriz)

                if proceso[key] == "mosaico":
                    copia = mosaicoSepia(matriz)
                    
            #Para los casos en que se invoque al menú de ayuda
            if key == "ayuda":
                #se excluye la generación de copias de la imagen
                copia = "nula"
                #luego según las decisiones del usuario se muestran los sub-menú pertinentes
                if proceso[key] == 1:
                    menuRetorno1()

                if proceso[key] == 2:
                    menuRetorno2()

                if proceso[key] == 3:
                    menuTiposDeTransformacion()

                if proceso[key] == 9:
                    menuAyuda()
                    
    
#
# SALIDA
#
    #Aún dentro del bucle impide finalizar el programa sin la decisión del usuario
    #si la copia es pertinente
    if copia != "nula":
        if proceso[key] != 0:
            #Se obtiene el nombre de la imagen original, sin su extensión
            nombreEscritura = list(nombreEntrada.split("."))

            #Se genera una copia de respaldo del original, por mera precaución y tranquilidad del usuario
            copiaExitosa = convertirMatrizAImagen(copiaOriginal, "copia.bmp")

            #Se informa de la creación correcta de la copia de respaldo
            print "El archivo copia.bmp se ha creado correctamente"

            #Para cada proceso de transformación que se ha solicitado
            for key in proceso:

                #Se genera la copia de la imagen transformada por el proceso respectivo
                #esta nueva copia, es nombrada igual al original, pero se agrega una extención
                #que indica el proceso por el cual fué sometida
                procesoExitoso = convertirMatrizAImagen(copia, nombreEscritura[0]+"_"+proceso[key]+".bmp")

                #si la copia y el proceso respectivo generaron las nuevas imagenes
                if copiaExitosa and procesoExitoso:
                    #Se informa al usuario de la creacion de estas
                    print "*******************************************************************************************"
                    print "El archivo "+nombreEscritura[0]+"_"+proceso[key]+".bmp se ha creado correctamente"
                    print "*******************************************************************************************"
                #En caso contrario
                else :
                    #Se envía en pantalla una advertencia sobre posibles errores que han impedido
                    #la creación de la nueva imagen
                    print "Error al leer ", nombreEntrada, "compruebe que la ruta y el nombre del archivo son correctos"

