series = 0

print('Fibonacci Sequence Generator')

n = int(input('Enter a number (max 15): '))

a = 1
b = 0
while (a < n):
	c = b
	b = a
	a = c + b
	print(a)