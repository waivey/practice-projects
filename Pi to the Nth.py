from math import pi

n = int(input('Select decimal place of pi up to 12:'))

print( format(pi, '.{}f'.format(n)) )
