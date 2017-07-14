from easy_math import factorial


def signo(x):
    return -1 if (x % 2 == 0) else 1


def trigonometrica_aprox(x, m, i):
    resultado = 0

    for n in range(1, m + 1):
        resultado += signo(n) * ((x ** i) / factorial(i))
        i += 2

    return resultado


def seno_aprox(x, m):
    return trigonometrica_aprox(x, m, 1)


def coseno_aprox(x, m):
    return trigonometrica_aprox(x, m, 0)


def error(f_exacta, f_aprox, m, x):
    return abs(f_exacta(x) - f_aprox(x, m))
