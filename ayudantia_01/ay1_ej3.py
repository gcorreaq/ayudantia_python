operand_1 = float(raw_input('Operando: ')) 
operator = str(raw_input('Operador: '))
operand_2 = float(raw_input('Operando: '))

if operator == '+':
    result = operand_1 + operand_2
elif operator == '-':
    result = operand_1 - operand_2
elif operator == '*':
    result = operand_1 * operand_2
elif operator == '/':
    result = operand_1 / operand_2
elif operator == '**':
    result = operand_1 ** operand_2
else:
    print 'Error! Operando incorrecto!'
    result = None

print operand_1, operator, operand_2, '=', result
