minutos_dia = int(raw_input("Minutos hablados DIA: "))
minutos_noche = int(raw_input("Minutos hablados NOCHE: "))

total = 0

print "DIA: ",

if minutos_dia > 100:
    minutos_dia -= 100

    print "excede en", minutos_dia, "minutos"

    total += (1000 + minutos_dia * 15)
else:
    print "no excede"
    total += minutos_dia * 10

print "NOCHE: ",

if minutos_noche > 80:
    minutos_noche -= 80

    print "excede en", minutos_noche, "minutos"

    total += (560 + minutos_noche * 13)
else:
    print "no excede"
    total += minutos_noche * 7

print "Cliente paga", total
