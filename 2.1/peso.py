peso_inicial = float(input('Introduzca su peso inicial: '))
peso_final = float(input('Introduzca su peso final: '))
meses = int(input('Introduzca el numero de meses: '))

bajar_por_mes = (peso_inicial - peso_final)/meses

print(f'Usted tendrá que bajar {bajar_por_mes} por mes')