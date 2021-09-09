from math import pi

r = float(input('Introduce el radio de la esfera: '))

area = round(4*pi*r**2,2)
volumen = round(4*pi*r**3/3,2)

print(f'área = {area}')
print(f'volumen = {volumen}')