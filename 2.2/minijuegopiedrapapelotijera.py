posibles = ['a', 'p', 't']

ana = input('Ana: ')
juan = input('Juan: ')

if len(ana) > 1 or len(juan)>1:
    print('Las tiradas deben de ser un caracter')
elif len(ana)==1 and len(juan)==1 and ana not in posibles or juan not in posibles:
    print('Tirada incorrecta')
else:
    if ana == 'a' and juan == 't':
        print('Gana Ana')
    if ana == 't' and juan == 'a':
        print('Gana Juan')
    if ana == 't' and juan == 'p':
        print('Gana Ana')
    if ana == 'p' and juan == 't':
        print('Gana Juan')
    if ana == 'p' and juan == 'a':
        print('Gana Ana')
    if ana == 'a' and juan == 'p':
        print('Gana Juan')
    if ana == juan:
        print('Empate')
        
        