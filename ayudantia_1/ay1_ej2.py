hour = int(raw_input('Hora:'))
meridiem = raw_input('AM o PM?: ')

if meridiem == 'am':
	print 'Buenos dias!'
elif meridiem == 'pm':
	if 8 <= hour <= 11:
		print 'Buenas noches!'
	else:
		print 'Buenas tardes!'
else:
	print 'Error!'
