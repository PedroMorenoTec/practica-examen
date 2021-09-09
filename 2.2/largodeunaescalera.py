from math import sin
from math import radians

altura = int(input('Altura de la casa en metros: '))
angulo = int(input('Ángulo de la escalera en grados: '))

largo=round(altura/sin(radians(angulo)))

print(f'El largo de la escalera es de {largo}')