print('==== DESAFIO 48 ====')
so = int(0)
for c in range(1, 501, 2):
    if c % 3 == 0:
        so = c + so
        print('{}..'.format(c), end='')
print('\nA soma dos números ímpares que são multiplos de três foi: {}'.format(so))
