numero_universidades = int(raw_input("Numero de universidades: "))

total_aceptan = 0
total_rechazan = 0
total_empates = 0

print ''

for universidad in range(numero_universidades):
    nombre_universidad = raw_input("Universidad: ")

    voto = ''
    aceptan = 0
    rechazan = 0
    blancos = 0
    nulos = 0

    while voto != 'X':
        voto = raw_input('Voto: ')

        if voto == 'A':
            aceptan += 1
        elif voto == 'R':
            rechazan += 1
        elif voto == 'B':
            blancos += 1
        elif voto == 'N':
            nulos += 1

    print nombre_universidad, ':', aceptan, 'aceptan,', rechazan, 'rechazan,', blancos, 'blancos,', nulos, 'nulos.\n'

    if aceptan > rechazan:
        total_aceptan += 1
    elif aceptan < rechazan:
        total_rechazan += 1
    else:
        total_empates += 1

print 'Universidades que aceptan:', total_aceptan
print 'Universidades que rechazan:', total_rechazan
print 'Universidades con empate:', total_empates