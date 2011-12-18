bishop_row = int(raw_input("Fila Alfil: "))
bishop_col = int(raw_input("Columna Alfil: "))
rook_row = int(raw_input("Fila Torre: "))
rook_col = int(raw_input("Columna Torre: "))

if rook_col == bishop_col or rook_row == bishop_row:
	print 'Torre captura'
else:
	col_difference = abs(bishop_col - rook_col)
	row_difference = abs(bishop_row - rook_row)

	if col_difference == 1 and row_difference == 1:
		print 'Alfil captura'
	else:
		# Para evitar problemas, siempre dejamos el numero menor como dividendo
		min_num = min(row_difference, col_difference)
		max_num = max(row_difference, col_difference)
		
		if 0 < (float(min_num) / max_num) % 1 < 1:
			print 'Ninguno captura'
		else:
			print 'Alfil captura'