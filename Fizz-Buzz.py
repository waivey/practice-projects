beg_rng = int(input('Pick a number between 1 and 10: '))

end_rng = int(input('Pick a number between 21 and 30: '))

for n in range(beg_rng, end_rng):
	if n % 3 == 0 and n % 5 == 0:
		print( 'Fizzbuzz!' )
	elif n % 3 == 0:
		print( 'Fizz' )
	elif n % 5 == 0:
		print( 'Buzz' )
	else:
		print( n ) 