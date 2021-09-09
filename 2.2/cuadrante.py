angulo = int(input('Dame un entero que se enecuentre entre 0 y 360 grados: '))

if(0 <= angulo <= 360):
    if angulo%90==0:
        print('eje')
    else:
        if 0 < angulo < 90:
            print('cuadrante 1')
        if 90 < angulo < 180:
            print('cuadrante 2')
        if 180 < angulo < 270:
            print('cuadrante 3')
        if 270 < angulo < 360:
            print('cuadrante 4')
else:
    print('excede')