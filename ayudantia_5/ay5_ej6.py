from easy_input import get_int

def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

tope = get_int("N: ")
print fibonacci(tope)