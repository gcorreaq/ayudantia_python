c1 = float(raw_input("C1: "))
c2 = float(raw_input("C2: "))

if c1 < 2.0 and c2 < 2.0:
    print "Reprobado"
elif c1 > 9.0 and c2 > 9.0:
    print "Aprobado"
else:
    c3 = float(raw_input("C3: "))

    promedio = (c1 + c2 + c3) / 3.0

    if promedio < 3.0:
        print "Reprobado"
    elif promedio > 7.0:
        print "Aprobado"
    else:
        examen = float(raw_input("Examen: "))

        if examen > 5.0:
            print "Aprobado"
        else:
            print "Reprobado"
