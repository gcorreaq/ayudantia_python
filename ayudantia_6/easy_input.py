def get_int(message):
	return int(raw_input(message))

def get_float(message):
	return float(raw_input(message))

def get_bool(message):
	return bool(raw_input(message))

def get_int_list(initial_message, exit_value):
    resultado = []

    print initial_message, '(Para terminar, ingrese <', exit_value, '> )'

    while True:
        data = raw_input('Ingrese numero: ')

        if data != exit_value:
            resultado.append(int(data))
        else
            break
    
    return resultado