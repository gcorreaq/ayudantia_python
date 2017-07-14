first_number = int(raw_input("Numero: "))
second_number = int(raw_input("Numero: "))

# Esto nos permite tener los numeros ordenados
if first_number > second_number:
    tmp = first_number
    first_number = second_number
    second_number = tmp

total = 0

# Se empieza a iterar despues del primer numero, hasta antes del segundo
for i in range(first_number + 1, second_number):
    total += i
    print i,

    # Con esto evitamos imprimir un signo mas adicional
    if i < (second_number - 1):
        print '+',

# Cuando termina, se imprime el signo igual y el total
print '=', total
