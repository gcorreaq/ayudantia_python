# encoding: utf-8

def misma_ciudad(u1, u2):
	user_1 = usuarios[u1]
	user_2 = usuarios[u2]

	return user_1[1] == user_2[1]

def diferencia_edad(u1, u2):
	user_1 = usuarios[u1]
	user_2 = usuarios[u2]

	return abs(user_1[2][0] - user_2[2][0])

####################
# Código de prueba #
####################

usuarios = {
	522514: ('Jean Dupont', 'Marseille', (1989, 11, 21)),
	587125: ('Perico Los Palotes', 'Valparaiso', (1990, 4, 12)),
	189471: ('Jan Kowalski', 'Krakow', (1994, 4, 22)),
	914210: ('Antonio Nobel', 'Valparaiso', (1983, 7, 1))
}

def main():
	print 'Misma ciudad >', misma_ciudad(914210, 587125)
	print 'Misma ciudad >', misma_ciudad(522514, 189471)
	print 'Diferencia de edad >', diferencia_edad(914210, 587125)

if __name__ == '__main__':
	main()
