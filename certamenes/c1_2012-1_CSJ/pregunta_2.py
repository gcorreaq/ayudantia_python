anotaciones = raw_input("Anotaciones: ")

# Descomentar esta linea y comentar la primera
# para probar mas rapido!
#anotaciones = 'DDTDLLDD DDLDT TDTLLD DDDDD'

puntaje_total = 0
puntaje_periodo = 0
periodo = 1

## Una opcion al 'for' que sigue es
#
# for letra in anotaciones:
##
for i in range(len(anotaciones)):
    letra = anotaciones[i]

    if letra == ' ':
        print puntaje_periodo, 'puntos en el periodo', periodo

        puntaje_total += puntaje_periodo
        periodo += 1
        puntaje_periodo = 0
    else:
        if letra == 'L':
            puntos = 1
        elif letra == 'D':
            puntos = 2
        elif letra == 'T':
            puntos = 3

        puntaje_periodo += puntos

# Al terminar, no hemos incluido el ultimo periodo
# por lo que lo incluimos ahora
print puntaje_periodo, 'puntos en el periodo', periodo
puntaje_total += puntaje_periodo

print 'Total:', puntaje_total, 'puntos'