def numero_de_seguidores(usuario, tuiton):
    total = 0

    for key, value in tuiton.items():
        if (key != usuario) and (usuario in value):
            total += 1

    return total


def son_amigos(usuario1, usuario2, tuiton):
    if (usuario1 in tuiton[usuario2]) and (usuario2 in tuiton[usuario1]):
        return True
    else:
        return False

    ## Una manera mas corta de hacerlo
    # return ((usuario1 in tuiton[usuario2]) and (usuario2 in tuiton[usuario1]))


####################
# Codigo de prueba #
####################
def main():
    tuiton = {
        # usuario: conjunto de usuarios a quienes sigue
        '@progra_usm': {'@kena123', '@anamontain'},
        '@luismi': {'@huaiqui', '@jvivar'},
        '@jvivar': {'@anamontain', '@progra_usm'},
        '@huaiqui': {'@anamontain', '@luismi'},
        '@anamontain': {'@luismi', '@progra_usm', '@huaiqui'},
        '@kena123': {'@luismi', '@huaiqui'}
    }

    print numero_de_seguidores('@luismi', tuiton)
    print son_amigos('@anamontain', '@huaiqui', tuiton)


if __name__ == '__main__':
    main()
