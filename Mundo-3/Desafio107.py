import móduloMoeda
print('==== DESAFIO 107 ====')

p = float(input('Digite o preço: '))

print(f'A metade de {p} é {móduloMoeda.metade(p)}')
print(f'O dobro de {p} é {móduloMoeda.dobro(p)}')
print(f'Aumentado em 10%, temos {móduloMoeda.aumentar(p, 10)}')
print(f'Reduzindo em 13%, temos {móduloMoeda.diminuir(p, 13)}')
