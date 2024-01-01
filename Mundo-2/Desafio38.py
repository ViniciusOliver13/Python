print('==== DESAFIO 38 ====')
nu1 = int(input('Digite um número: '))
nu2 = int(input('Digite outro número: '))
if nu1 > nu2:
    print('O 1º valor é maior do que {}.'.format(nu2))
elif nu2 > nu1:
    print('O 2º valor é maior do que {}.'.format(nu1))
else:
    print('Não existe valor maior. Os dois são iguais.')
