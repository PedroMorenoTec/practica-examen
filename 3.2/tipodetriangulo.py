print('Introduzca tres números enteros')
x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))

if(x+y>z and x+z>y and y+z>x and x>0 and y>0 and z>0):
    if(x != y != z):
        print('ESCALENO')
    elif(x == y == z):
        print('EQUILATERO')
    else:
        print('ISOCELES')
else:
    print('NO ES TRIANGULO')