# coding: UTF-8


year = int(raw_input("Ingrese un año: "))

if year % 400 == 0:
    print year, 'es bisiesto'
elif year % 100 != 0 and year % 4 == 0:
    print year, 'es bisiesto'
else:
    print year, 'no es bisiesto'
