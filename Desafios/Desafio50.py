print('==== DESAFIO 50 ====')
soma = int(0)
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
print('O valor da soma dos pares foi: {}'.format(soma))
