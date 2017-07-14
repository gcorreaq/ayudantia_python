def mapping(data, function):
    for element in data:
        function(element)


def var_dump(variable):
    var_type = type(variable)
    print var_type, variable,

    if var_type == str:
        print ', Size:', len(variable)
    else:
        print ''


def show_truncated(string):
    if len(string) <= 10:
        print string
    else:
        # Aca usamos un slice!
        print "%(string)s..." % {"string": string[0:10]}


def main():
    a = ['Hola', 123, -0.341, True, (1, 2, 3)]
    b = ["Esto es un mensaje muy largo", "Msj Corto!", "Otro Msj", "LALALALALALALALA"]

    # Mostrar tipos de datos
    mapping(a, var_dump)

    # Mostrar strings cortados
    mapping(b, show_truncated)


if __name__ == '__main__':
    main()
