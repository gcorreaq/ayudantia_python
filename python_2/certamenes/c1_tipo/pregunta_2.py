a = float(raw_input("Ingrese A: "))
b = float(raw_input("Ingrese B: "))
c = float(raw_input("Ingrese C: "))

# Comprobamos todas las sumas posibles
if (c > (a + b)) or (a > (b + c)) or (b > (a + c)):
    print 'No es un triangulo valido'
else:
    # Comprobamos tipo de triangulo

    # Si todos los lados son iguales, es equilatero
    if a == b == c:
        print 'Triangulo equilatero'
    # Si dos lados son iguales, es isosceles
    elif a == b or b == c or c == a:
        print 'Triangulo isosceles'
    # Si ninguna condicion anterior es verdadera
    # entonces todos los lados son distintos y
    # el triangulo es escaleno
    else:
        print 'Triangulo escaleno'
