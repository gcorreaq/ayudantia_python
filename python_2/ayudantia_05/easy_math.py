def factorial(n):
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado


def divisible(numero, divisor):
    return numero % divisor == 0


def mcd(a, b):
    actual_mcd = 1

    for div in range(1, min(a, b) + 1):
        if (a % div == 0) and (b % div == 0):
            actual_mcd = div

    return actual_mcd
