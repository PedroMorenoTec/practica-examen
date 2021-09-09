from math import sqrt

r = float(input('Radio: '))
Cx = float(input('Centro x: '))
Cy = float(input('Centro y: '))
Px = float(input('Punto x: '))
Py = float(input('Punto y: '))

d = sqrt((Py - Cy)**2 + (Px - Cx)**2)

if d==r:
    print('SOBRE')
if d<r:
    print('DENTRO')
if d>r:
    print('FUERA')