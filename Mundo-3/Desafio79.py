print('==== DESAFIO 79 ====')
numpy = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numpy:
        print('Valor adicionado!')
        numpy.append(n)
    else:
        print('O valor já está na lista!')
    escolha = str(input('Você quer continuar? [S/N]')).lower()
    if 'n' in escolha:
        print('Laço encerrado!')
        break
print(f'Valores da lista em ordem crescente: {sorted(numpy)}')
