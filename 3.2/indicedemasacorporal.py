peso = float(input('Peso en kg: '))
altura = float(input('Altura en m: '))

indice = round(peso / altura**2,2)

print(indice)

if indice < 20:
    print('PESO BAJO')
if 20 <= indice < 25:
    print('NORMAL')
if 25 <= indice < 30:
    print('SOBREPESO')
if 30 <= indice < 40:
    print('OBESIDAD')
if indice >= 40:
    print('OBESIDAD MORBIDA')