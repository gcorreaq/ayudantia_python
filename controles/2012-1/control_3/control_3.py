cant_grupos = int(raw_input("Ingrese grupos: "))

mayor_promedio = 0
mayor_nota = 0
mejor_grupo = 0
grupo_mejor_nota = 0

for grupo in range(1, cant_grupos + 1):

    cant_integrantes = int(raw_input("Cantidad grupo {0}: ".format(grupo)))

    suma_notas = 0

    for alumno in range(1, cant_integrantes + 1):
        nota = int(raw_input("Alumno {0}: ".format(alumno)))

        if nota > mayor_nota:
            mayor_nota = nota
            grupo_mejor_nota = grupo

        suma_notas += nota

    promedio = suma_notas / cant_integrantes

    if promedio > mayor_promedio:
        mayor_promedio = promedio
        mejor_grupo = grupo

    print "Nota del grupo: {0}".format(promedio)

print "El mejor grupo fue el {0}".format(mejor_grupo)
print "La nota mas alta la obtuvo un integrante del grupo {0}".format(grupo_mejor_nota)