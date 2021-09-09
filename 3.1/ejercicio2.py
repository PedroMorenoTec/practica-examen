print('Introduzca los lados del triángulo')
x = float(input('x: '))
y = float(input('y: '))
z = float(input('z: '))

if(x+y>z and x+z>y and y+z>x and x>0 and y>0 and z>0):
    if(x != y != z):
        print('El tríangulo es escaleno')
    elif(x == y == z):
        print('El tríangulo es equilátero')
    else:
        print('El tríangulo es isóceles')
else:
    print('El triángulo no existe')
