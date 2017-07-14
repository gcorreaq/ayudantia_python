def menor_minima(temperaturas):
    minima = ('', 100)

    for comuna, temps in temperaturas.items():
        if temps[0] < minima[1]:
            minima = (comuna, temps[0])

    return minima