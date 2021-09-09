n = int(input('Introduce un número entero: '))

suma_divisores=0
i=1
while i<=int(n/2):
    if n%i==0:
        suma_divisores+=i
    i+=1

if suma_divisores == n:
    print('El número es perfecto')