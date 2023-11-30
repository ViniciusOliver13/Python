print('==== DESAFIO 67 ====')
n = int(input('Quer ver a tabuada de qual número? '))
while n >= 0:
    cont = 1
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    n = int(input('Quer ver a tabuada de qual número? '))
print('Acabou')
