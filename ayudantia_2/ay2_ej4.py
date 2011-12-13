num = int(raw_input("N: "))

total = 0.0
actual = 1.0

for i in range(1, num + 1):

	element = (1.0 / actual)

	if i % 2 == 0:
		element = - element

	total += element
	actual += 2.0

print (4.0 * total)