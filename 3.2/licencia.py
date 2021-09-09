edad = int(input('Edad: '))
tiene_identificacion = input('¿Tiene identificacion? (s/n) ')

if(edad>=18 and tiene_identificacion=='s'):
    print('Si')
else:
    print('No')