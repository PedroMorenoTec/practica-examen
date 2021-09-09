year = int(input('Introduce un año mayor a cero: '))

if(year%4==0 and (year%100!=0 or year%400==0)):
    print(True)
else:
    print(False)