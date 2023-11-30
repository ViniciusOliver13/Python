print('==== DESAFIO 51 ====')
num = int(input('Qual é o primeiro termo da PA? '))
r = int(input('Qual é a razão? '))
term = num + (10 - 1) * r
for c in range(num, term + r, r):
    print('{} -> '.format(c), end='')
print('ACABOU')