destino = raw_input("Destino: ")
autonomia = int(raw_input("Autonomia: "))

if destino == 'C':
    distancia_total = 21
elif destino == 'B':
    distancia_total = 16

distancia_recorrida = autonomia

while distancia_recorrida < distancia_total:

    if distancia_recorrida == 5:
        distancia_recorrida -= 1

    if destino == 'C':
        if distancia_recorrida == 14:
            distancia_recorrida -= 1

    print 'Acampa en km', distancia_recorrida

    distancia_recorrida += autonomia

print 'Llega a', destino