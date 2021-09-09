mensajes = int(input('Introduzca el número de mensajes: '))
megas = float(input('Introduzca el número de megas: '))
minutos = float(input('Introduzca el número de minutos: '))

costo = (mensajes + megas + minutos) * 0.8

print(f'El costo mensual es {costo}')