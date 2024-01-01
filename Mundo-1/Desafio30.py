print('==== DESAFIO 30 ====')
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O número \033[4;36m{}\033[m é PAR!'.format(num))
else:
    print('O número \033[4;35m{}\033[m é ÍMPAR!'.format(num))
