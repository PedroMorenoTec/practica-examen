from math import sqrt

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

if a==b==0:
    print('No tiene solución')
elif a==0 and b!=0:
    print(f'x= {round(-c/b,2)}')
elif a!=0 and b!=0:
    discriminante = b**2-4*a*c
    if discriminante<0:
        print('Raíces complejas')
    elif discriminante>0:
        x1 = round((-b+sqrt(discriminante))/2,2)
        x2 = round((-b-sqrt(discriminante))/2,2)
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
    elif discriminante==0:
        x = round((-b+sqrt(discriminante))/2,2)
        print(f'x = {round(b/(2*a),2)}')

        
