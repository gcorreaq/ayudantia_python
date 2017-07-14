def obtener_dominios(c):
	dominios = set()

	for email in c:
		dominios.add(email.split('@')[-1])

	return list(dominios)

def contar_tld(c):
	tlds = {}

	for email in c:
		tld = email.split('.')[-1]

		if tld not in genericos:
			if tld in tlds:
				tlds[tld] += 1
			else:
				tlds[tld] = 1

	return tlds

####################
# Codigo de prueba #
####################
genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}
c = [
	'fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net',
	'gudrun@lala.de', 'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl',
	'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl', 'gonchi@codegears.cl',
	'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com',
	'fer@x.com', 'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl'
]

print obtener_dominios(c)
print contar_tld(c)