series = 0

print('Fibonacci Sequence Generator')

n = int(input('Enter a number (max 15): '))

sequence = [0, 1]

a = 1
b = 0
while (a < n):
	c = b
	b = a
	a = c + b
	sequence.append(a)

print( sequence )

