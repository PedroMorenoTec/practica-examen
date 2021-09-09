n = int(input('Introduzca un número entero: '))

if n>=0 and n%2==0:
    print(f'{n} es par positivo')
if n>=0 and n%2==1:
    print(f'{n} es impar positivo')
if n<0 and n%2==0:
    print(f'{n} es par negativo')
if n<0 and n%2==1:
    print(f'{n} es impar negativo')