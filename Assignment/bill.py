units = int(input('Enter the amount of units used:'))

if units <= 100:
	print('Bill amount = ' + str(units * 2))
elif units > 100 and units <= 200:
	print('Bill amount = ' + str(units * 3))
elif units > 200 and units <= 300:
	print('Bill amount = ' + str(units * 5))
else:
	print('Bill amount = ' + str(units * 6))
