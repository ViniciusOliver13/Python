import móduloMoeda
print('==== DESAFIO 108 ====')

p = float(input('Digite o preço: R$'))

print(f'A metade de {móduloMoeda.moeda(p)} é {móduloMoeda.moeda(móduloMoeda.metade(p))}')
print(f'O dobro de {móduloMoeda.moeda(p)} é {móduloMoeda.moeda(móduloMoeda.dobro(p))}')
print(f'Aumentado em 10%, temos {móduloMoeda.moeda(móduloMoeda.aumentar(p, 10))}')
print(f'Reduzindo em 13%, temos {móduloMoeda.moeda(móduloMoeda.diminuir(p, 13))}')
