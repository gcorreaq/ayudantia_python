anno = int(raw_input("Anno: "))
mes = int(raw_input("Mes: "))
dia = int(raw_input("Dia: "))

anno_actual = 2012
mes_actual = 5
dia_actual = 10

annos = anno_actual - anno
meses = mes_actual - mes

if meses < 0:
    annos -= 1
    meses += 12

dias = dia_actual - dia

if dias < 0:
    if meses == 0:
        annos -= 1
        meses = 11
    else:
        meses -= 1

    dias += 30

print 'Edad:', annos, 'annos,', meses, 'meses,', dias, 'dias.'
