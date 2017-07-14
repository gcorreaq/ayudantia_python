# Buscaminas
from numpy import *


def crear_campo(forma, n):
    # Se sacan las dimensiones
    alto, ancho = forma

    # Primero, se crea una lista de (alto * ancho)
    # ceros, restandole los unos que se van a agregar
    ceros = list(zeros((alto * ancho) - n))

    # Se crea una lista de 'n' unos (negativos!)
    unos = list(-1 * ones(n))

    # Se juntan las listas, y se transforman en arrays
    campo = array(unos + ceros)

    # Se mezcla el array
    random.shuffle(campo)

    # Se le cambia la forma a la deseada
    campo = campo.reshape((alto, ancho))

    return campo


# Esto se puede reducir a
# campo = array(list(zeros((alto * ancho) - n)) + list(ones(n)))
# random.shuffle(campo)
# return campo.reshape((alto, ancho))

def descubrir(campo):
    alto, ancho = campo.shape

    # Se recorre todo el campo
    for i in range(0, alto):
        for j in range(0, ancho):
            # Solo aplicaremos el algoritmo cuando
            # encontremos una mina
            if campo[i][j] == -1:
                # Condiciones de borde
                if i > 0:
                    start_x = -1
                else:
                    start_x = 0

                if i < (alto - 1):
                    end_x = 2
                else:
                    end_x = 1

                if j > 0:
                    start_y = -1
                else:
                    start_y = 0

                if j < (ancho - 1):
                    end_y = 2
                else:
                    end_y = 1

                # Se empieza a recorrer alrededores
                for x in range(start_x, end_x):
                    for y in range(start_y, end_y):

                        # Para evitar modificar la misma mina
                        if (x != 0) or (y != 0):
                            # Coordenadas a moverse
                            vertical = i + x
                            horizontal = j + y

                            # Si no es mina, se aumenta numero
                            if campo[vertical][horizontal] != -1:
                                campo[vertical][horizontal] += 1

    return campo


####################
# Codigo de prueba #
####################
def main():
    # Mismo campo que ejemplo
    c = array([[0, 0, -1, -1],
               [0, 0, -1, 0],
               [0, 0, 0, -1],
               [0, 0, 0, -1]])

    # Para comprobar ejemplo
    print descubrir(c)

    # Para probar con campo generado
    c_generado = crear_campo((4, 4), 5)
    print c_generado
    print descubrir(c_generado)


if __name__ == '__main__':
    main()
