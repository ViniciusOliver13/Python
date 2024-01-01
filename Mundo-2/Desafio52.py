print('==== DESAFIO 52 ====')
num = int(input('Digite um número: '))
cont = int(0)
res = 'O NÚMERO {} NÃO É PRIMO!'.format(num)
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1
if cont == 2:
    res = 'O NÚMERO {} É PRIMO!'.format(num)
print(res)
