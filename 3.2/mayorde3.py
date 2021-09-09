print('Introduzca tres números enteros')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

mayor = float('-inf')

if(x>mayor):
    mayor=x
if(y>mayor):
    mayor=y
if(z>mayor):
    mayor=z

print(f'El número mayor es {mayor}')