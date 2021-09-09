bultos = float(input('Cantidad de bultos de cemento: '))
precio = float(input('Precio por bulto de cemento: '))

precio = bultos * precio
print(f'El precio antes de impuestos es de: {precio}')

impuestos = precio * 0.16
print(f'Los impuestos son de: {impuestos}')

precio_con_impuestos = precio + impuestos
print(f'El precio después de impuestos es de: {precio_con_impuestos}')
