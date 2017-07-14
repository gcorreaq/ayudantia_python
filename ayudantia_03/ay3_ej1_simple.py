bishop_row = int(raw_input("Alfil, Fila: "))
bishop_col = int(raw_input("Alfil, Columna: "))
rook_row = int(raw_input("Torre, Fila: "))
rook_col = int(raw_input("Torre, Columna: "))

if rook_col == bishop_col or rook_row == bishop_row:
    print 'Torre captura alfil'
elif abs(bishop_row - rook_row) == abs(bishop_col - rook_col):
    print 'Alfil captura torre'
else:
    print 'Ninguno captura'
