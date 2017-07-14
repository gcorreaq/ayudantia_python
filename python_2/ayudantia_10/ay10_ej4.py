# Funcion a modo de 'helper' (ayuda) para
# centralizar la extraccion de los numeros
def transform_data(row):
    return map(int, row.strip().split(' '))


# La idea es contar la cantidad de lineas del
# archivo
def contar_cartones():
    archivo = open(nombre_archivo)
    contador = 0

    for linea in archivo:
        contador += 1

    archivo.close()
    return contador


# Si el numero se encuentra en una
# linea, entonces esta en un carton
# y se contabiliza
def contar_numero_de_cartones(n):
    archivo = open(nombre_archivo)
    contador = 0

    for linea in archivo:
        carton = transform_data(linea)
        if n in carton:
            contador += 1

    archivo.close()
    return contador


# Basta con encontrar un carton ganador
# para retornar True o False
def hay_ganadores(numeros):
    archivo = open(nombre_archivo)

    for linea in archivo:
        # Ya que los numeros son un Set
        # se transforman los numeros del carton
        # en Set para compararlos
        carton = set(transform_data(linea))

        if numeros == carton:
            # Notar que antes de hacer el return
            # se cierra el archivo
            archivo.close()
            return True

    archivo.close()
    return False


# Basta con contar cuantos de los
# numeros jugados estan en cada carton
# y ver si la cantidad es igual a 'n'
def n_aciertos(numeros, n):
    archivo = open(nombre_archivo)
    cant_cartones = 0

    for linea in archivo:
        carton = transform_data(linea)
        contador = 0

        for numero in numeros:
            if numero in carton:
                contador += 1

        if contador == n:
            cant_cartones += 1

        # Esta es una alternativa mas corta
        # al codigo entre las lineas 45 y 54
        # carton = set(carton)
        #
        # if len(numeros & carton) == n:
        #	cant_cartones += 1

    archivo.close()
    return cant_cartones


####################
# Codigo de prueba #
####################

# Esto es para tener un archivo comun para todas las funciones
nombre_archivo = 'juegos.txt'

# Los ejemplos son con datos de la pagina
print 'Cantidad de cartones:', contar_cartones()
print 'Cantidad de cartones con el numero 7:', contar_numero_de_cartones(7)
print 'Numeros jugados:', {13, 33, 5, 38, 1, 19}
print 'Hay ganadores?:', hay_ganadores({13, 33, 5, 38, 1, 19})
print 'Numeros jugados:', {14, 21, 1, 36, 9, 17}
print 'Hay ganadores?:', hay_ganadores({14, 21, 1, 36, 9, 17})
print '- Prueba de aciertos -'
print 'Numeros:', {20, 39, 6, 27, 12, 4}, ' y 3 aciertos:', n_aciertos({20, 39, 6, 27, 12, 4}, 3)
print 'Numeros:', {13, 33, 5, 38, 1, 19}, ' y 4 aciertos:', n_aciertos({13, 33, 5, 38, 1, 19}, 4)
print 'Numeros:', {1, 2, 3, 4, 5, 6}, ' y 5 aciertos:', n_aciertos({1, 2, 3, 4, 5, 6}, 5)
