n = int(input('Introduce un entero positivo: '))

msg=''

for i in range(1, n+1):
    msg+=str(i) + ', '
    
for i in range(n-1, 0, -1):
    msg+=str(i) + ', '
    
msg = msg[:-2]

print(msg)