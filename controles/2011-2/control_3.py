# Control 3

success = 0

for i in range(3):
    # Este valor es arbitrario, y solo para poder entrar a los 'while'
    num1 = 0
    num2 = 0

    # Se pedira el numero hasta que cumpla la condicion
    while not (10 < num1 < 100):
        num1 = int(raw_input("Numero 1: "))

        # Mensaje de error en caso de que numero sea invalido
        if not (10 < num1 < 100):
            print 'Numero invalido!'

    # Se pedira el numero hasta que cumpla la condicion
    while not (10 < num2 < 100):
        num2 = int(raw_input("Numero 2: "))

        # Mensaje de error en caso de que numero sea invalido
        if not (10 < num2 < 100):
            print 'Numero invalido!'

    # Si al calcular modulo 2 los resultados son distintos,
    # entonces uno es par y el otro impar
    if (num1 % 2) != (num2 % 2):
        print 'Exitoso'
        success += 1
    else:
        print 'No exitoso'

print 'Usted ha',

if success == 2 or success == 3:
    print 'ganado'
else:
    print 'perdido'
