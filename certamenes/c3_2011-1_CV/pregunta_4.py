from numpy import *

def reducir(img, f):
	filas, columnas = img.shape
	img_reducida = []

	inicio_fila = 0
	fin_fila = f

	for i in range(filas / f):
		inicio_columna = 0
		fin_columna = f

		for j in range(columnas / f):
			rebanada = img[inicio_fila:fin_fila, inicio_columna:fin_columna]
			img_reducida.append(sum(rebanada) / float(rebanada.size))

			inicio_columna += f
			fin_columna += f

		inicio_fila += f
		fin_fila += f

	img_reducida = array(img_reducida).reshape((filas / f, columnas / f))
	return img_reducida.astype(int)

def binarizar(img, umbral):
	img_lineal = img.reshape((1, img.size))

	for pixel in range(img.size):
		if img_lineal[0][pixel] >= umbral:
			# Blanco
			nuevo_valor = 255
		else:
			# Negro
			nuevo_valor = 0

		img_lineal[0][pixel] = nuevo_valor

	return img_lineal.reshape(img.shape)

def generar_imagen(alto, ancho):
	img = random.random((alto, ancho)) * 255
	return img.astype(int)

####################
# Codigo de prueba #
####################

def main():
	# Se genera imagen al azar
	imagen = generar_imagen(10, 10)
	print imagen
	print reducir(imagen, 5)
	print binarizar(imagen, 190)

if __name__ == '__main__':
	main()