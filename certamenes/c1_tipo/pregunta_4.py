# Parametros dados en el enunciado

# El enunciado dice que estos valores
# es mejor tratarlos como numeros reales
x = 300.0
y = 400.0

alfa = 3e-2
beta = 4e-5
gamma = 5e-2
delta = 6e-6

# Partimos en el dia cero
dias = 0

# Repetimos el proceso mientras queden conejos
while y >= 1:
    # Formulas para el cambio en las poblaciones
    delta_x = x * (alfa - beta * y)
    delta_y = -y * (gamma - delta * x)

    # Aplicamos el cambio a cada poblacion
    x += delta_x
    y += delta_y

    # Ha pasado un dia
    dias += 1

print 'Los conejos se extinguiran en', dias