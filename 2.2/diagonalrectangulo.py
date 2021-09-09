from math import sqrt

a = float(input('Ancho: '))
l = float(input('Largo: '))

diagonal = sqrt(a**2 + l**2)

print(f'La diagonal es {diagonal}')