from math import e

poblacion_inicial = int(input('Poblacion incial: '))
tiempo = int(input('Tiempo en años: '))
tasa = float(input('Tasa de crecimiento: '))

poblacion_final = int(poblacion_inicial*e**(tasa*tiempo))

print(f'La población final sera {poblacion_final}')