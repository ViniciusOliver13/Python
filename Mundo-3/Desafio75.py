print('==== DESAFIO 75 ====')
tuple = ((int(input('Digite um número: '))), (int(input('Digite um número: '))),
         (int(input('Digite um número: '))), (int(input('Digite um número: '))))
print(f'Valores digitados : {tuple}\nO número 9 apareceu {tuple.count(9)} vezes.')
if 3 in tuple:
    print(f'O número 3 apareceu na primeira vez na posição {tuple.index(3) + 1}.')
else:
    print('O número 3 não está presente na tupla!')
print('Os valores pares foram ', end='')
for i in tuple:
    if i % 2 == 0 and i != 0:
        print(f'{i}', end=' ')
