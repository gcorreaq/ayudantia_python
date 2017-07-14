from pregunta_3 import son_amigos


def usuario_con_mas_seguidores(tuiton):
    mayor = -1
    lista_de_usuarios = tuiton.keys()

    for usuario1 in lista_de_usuarios:
        total_usuario = 0
        for usuario2, seguidos in tuiton.items():
            if usuario1 != usuario2:
                if usuario1 in seguidos:
                    total_usuario += 1

        if total_usuario > mayor:
            mayor = total_usuario
            ganador = usuario1

    return (ganador, mayor)


def usuarios_sin_amigos(tuiton):
    usuarios = []

    for usuario1, seguidos in tuiton.items():
        tiene_amigos = False  # Forever Alone

        for usuario2 in seguidos:
            if son_amigos(usuario1, usuario2, tuiton):
                tiene_amigos = True
                break

        if not tiene_amigos:
            usuarios.append(usuario1)

    return usuarios


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

    print usuario_con_mas_seguidores(tuiton)
    print usuarios_sin_amigos(tuiton)


if __name__ == '__main__':
    main()
