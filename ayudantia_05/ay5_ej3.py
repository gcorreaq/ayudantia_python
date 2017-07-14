# Importamos las funciones que necesitemos
from easy_input import get_int


# Funciones para este programa
def mcd(a, b):
    div = 1
    actual_mcd = 1

    # Notar que esto podria hacerse con 'for'
    # Ver modulo 'easy_math.py' para ver ejemplo
    while div < min(a, b):
        div += 1

        if (a % div == 0) and (b % div == 0):
            actual_mcd = div

    return actual_mcd


# Codigo del programa
a = get_int("A: ")
b = get_int("B: ")

print mcd(a, b)
