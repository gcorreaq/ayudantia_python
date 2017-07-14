def contar_letras(string):
    string = string.lower()
    result = {}

    for token in string:
        if token != ' ':
            if token not in result:
                result[token] = 1
            else:
                result[token] += 1

    return result


def contar_vocales(string):
    string = string.lower()
    result = {}

    for token in string:
        if token != ' ':
            if token in ['a', 'e', 'i', 'o', 'u']:
                if token not in result:
                    result[token] = 1
                else:
                    result[token] += 1

    return result


def contar_iniciales(string):
    string = string.lower()
    splitted = string.split()
    result = {}

    for token in splitted:
        if token != '':
            initial = token[:1]

            if initial not in result:
                result[initial] = 1
            else:
                result[initial] += 1

    return result


def contar_palabras(string):
    string = string.lower()
    splitted = string.split()
    result = {}

    for word in splitted:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    return result


def main():
    string = raw_input("Ingrese frase: ")
    print contar_letras(string)
    print contar_vocales(string)
    print contar_iniciales(string)
    print contar_palabras(string)


if __name__ == '__main__':
    main()
