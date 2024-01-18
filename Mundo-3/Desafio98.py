from operator import neg
from time import sleep


def contador(i, f, p):
    sleep(1)
    print('=-' * 30)
    print(f'Contagem de {i} até {f}, de {abs(p)} em {abs(p)}:')

    if p == 0:
        p = 1
        
    if i > f and p > 0:
        p = neg(p)

    if p < 0:
        f = f - 1

    else:
        f = f + 1

    for c in range(i, f, p):
        print(f'{c} ', end='')
        sleep(0.4)
    print('FIM!')


print('==== DESAFIO 98 ====')
escolha = dict()
contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
