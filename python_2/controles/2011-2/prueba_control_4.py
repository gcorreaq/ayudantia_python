# Este archivo es solo para probar las funciones del control 4
from control_4 import suma_digitos, reducir_a_digito


def main():
    # Prueba de suma de digitos
    print "-- Suma de digitos --"
    numero = int(raw_input("Numero: "))

    print suma_digitos(numero)

    # Prueba de reducir a digito
    print "-- Reducir a digito --"
    numero = int(raw_input("Numero: "))

    print reducir_a_digito(numero)


if __name__ == '__main__':
    main()
