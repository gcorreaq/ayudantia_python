money = int(raw_input('Cuanto dinero tienes?: '))
products = raw_input('Que productos quieres?: ')

total = 0

# Sopaipillas
if 'sopaipilla' in products:
    total += 100

# Yogurt
if 'yogurt' in products:
    total += 200

# Completo italiano
if 'italiano' in products:
    total += 500

# Kapo
if 'kapo' in products:
    total += 200

# Ferrari
if 'ferrari' in products:
    total += 50000000

difference = money - total

if difference > 0:
    print 'Te alcanza y te sobran ', difference
elif difference == 0:
    print 'Te alcanza pero quedas pato!'
else:
    print 'No te alcanza, te faltan', abs(difference)
