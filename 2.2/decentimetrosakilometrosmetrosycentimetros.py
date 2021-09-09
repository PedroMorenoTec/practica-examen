distancia = int(input('Introduzca una distancia: '))

km = distancia // (1*10**5)
distancia%=(1*10**5)

m = distancia // (1*10**2)
distancia%=(1*10**2)

cm = distancia

if km>0:
    print(f'{km} km')
if m>0:
    print(f'{m} m')
if cm>0:
    print(f'{cm} cm')