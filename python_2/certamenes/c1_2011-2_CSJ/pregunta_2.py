distancia = float(raw_input("Distancia: "))
angulo = float(raw_input("Angulo: "))

# Primero angulo, para descartar PUBLICO
if 0 <= distancia <= 7:
    print 'PILETA'
elif 45 < angulo <= 90:
    print 'PUBLICO'
elif distancia > 47:
    print 'FUERA DE LA PLAZA'
else:
    if (0 <= angulo <= 45) or (90 < angulo <= 135) or (180 < angulo <= 225) or (270 < angulo <= 315):
        if 20 < distancia <= 35:
            print 'AREA VERDE'
        elif distancia <= 47:
            print 'CEMENTO'
    else:
        print 'CEMENTO'
