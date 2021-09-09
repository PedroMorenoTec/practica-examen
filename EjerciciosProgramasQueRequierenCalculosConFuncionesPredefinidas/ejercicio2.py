from math import sqrt

print('Introduce los lados de un triángulo')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

s = (a+b+c)/2
area = round(sqrt(s*(s-a)*(s-b)*(s-c)),2)

print(f'El área del triángulo es {area}')