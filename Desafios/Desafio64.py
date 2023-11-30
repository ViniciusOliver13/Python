print('==== DESAFIO 64 ====')
soma = cont = 0
num = int(input('Digite um número: '))
while not num == 999:
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print('A soma de todos os números foi {} de um total de {} números.'.format(soma, cont))
