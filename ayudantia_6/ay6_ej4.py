from easy_input import get_int

def add_movie(movies_list):
    name = raw_input("Nombre: ")
    year = get_int("Estreno: ")

    movies_list.append((name, year))

def delete_movie(movies_list):
    # Nombre exacto de la pelicula
    name = raw_input("Nombre: ")
    index = 0

    for movie in movies_list:
        m_name, _ = movie

        if m_name == name:
            break;
        
        index += 1
    
    del movies_list[index]

def search_movie(movies_list):
    name = raw_input("Nombre: ")

    for movie in movies_list:
        m_name, m_year = movie

        if m_name == name:
            print m_name, '(', m_year, ')'
            break

def show_all(movies_list):
    print 'Lista de todas las peliculas'
    print ''
    print movies_list

def main():

    peliculas = []

    while True:
        print '------'
        print '1) Agregar pelicula'
        print '2) Eliminar pelicula'
        print '3) Buscar pelicula'
        print '4) Mostrar todas las peliculas'
        print '5) Salir'

        opcion = get_int("Opcion: ")

        if opcion == 1:
            add_movie(peliculas)
        elif opcion == 2:
            delete_movie(peliculas)
        elif opcion == 3:
            search_movie(peliculas)
        elif opcion == 4:
            show_all(peliculas)
        elif opcion == 5:
            break
        else:
            print 'Opcion no valida'

        peliculas.sort()
    
    raw_input('Terminado. Enter para salir...')

if __name__ == '__main__':
    main()