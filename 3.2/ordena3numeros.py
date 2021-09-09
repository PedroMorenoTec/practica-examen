print('Introduzca tres números enteros')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

arr = [x,y,z]

for i in range(0, len(arr)):
    menor = arr[i]
    for j in range(i, len(arr)):
        if(arr[j]<menor):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print(arr)