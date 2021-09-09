year = int(input('Año: '))
mes = int(input('Mes: '))
dia = int(input('Día: '))

dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year%4==0 and (year%100!=0 or year%400==0):
    dias_del_mes[2-1]=29

if(dia == dias_del_mes[mes-1]):
    if mes == 12:
        year+=1
        dia=1
        mes=1      
    else:
        dia=1
        mes+=1
else:
    dia+=1

print(year)
print(mes)
print(dia)
