s=0
c=0

while s<1000:
    n = int(input('Introduce un número entero a sumar: '))
    s+=n
    c+=1
    
print(f'suma = {s}')
print(f'cantidad de números = {c}')