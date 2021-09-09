area = float(input('Area a pintar: '))
rendimiento = float(input('Cantidad de metros cuadrados que se pueden cubrir con un litro de pintura: '))

litros_a_pintar = round(area/rendimiento)

print(f'La cantidad de litros a pintar es {litros_a_pintar}')