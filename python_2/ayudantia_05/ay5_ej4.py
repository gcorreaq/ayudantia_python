from easy_input import get_int, get_float
from trigonometricas import seno_aprox, coseno_aprox, error
from math import sin, cos

angulo = get_float("Angulo en radianes: ")
terminos = get_int("Cant. de terminos: ")

seno = seno_aprox(angulo, terminos)
print 'Seno aproximado: ', seno
print 'Seno real: ', sin(angulo)
print 'Error: ', error(sin, seno_aprox, terminos, angulo)

coseno = coseno_aprox(angulo, terminos)
print 'Coseno aproximado: ', coseno
print 'Coseno real: ', cos(angulo)
print 'Error: ', error(cos, coseno_aprox, terminos, angulo)
