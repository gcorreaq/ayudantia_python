def bubble_sort(lista):
    # Esto es para iniciar el while
    cambio = True
    # Lo hacemos aca para no repetirlo en cada iteracion del while
    rango = range(1, len(lista))

    while cambio:
        cambio = False

        for i in rango:
            if lista[i - 1] > lista[i]:
                tmp = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = tmp
                cambio = True

def main():
    num = 0
    lista = []

    while num != 'ok':
        num = raw_input("Numero ('ok' para terminar): ")

        if num == 'ok':
            break
        else:
            lista.append(int(num))

    print 'Numeros desordenados ->', lista
    bubble_sort(lista)
    print 'Numeros ordenados ->', lista

if __name__ == "__main__":
    main()