print('==== DESAFIO 86-87 ====')
matriz = [[], [], []]
soma = pares = 0

for linhas in range(0, 3):
    for colunas in range(0, 3):
        matriz[linhas].append(int(input(f'Informe o número da posição[{linhas}][{colunas}]: ')))

        if matriz[linhas][colunas] % 2 == 0:
            pares += matriz[linhas][colunas]

        if colunas == 2:
            soma += matriz[linhas][colunas]

print('=-' * 20)
for linhas in range(0, 3):
    for colunas in range(0, 3):
        print(f'[{matriz[linhas][colunas]:^5}] ', end='')
    print('')
print('=-' * 20)
print(f'A soma dos valores Pares digitados foi {pares}.')
print(f'A soma dos valores da 3º coluna foi {soma}.')
print(f'O maior valor da 2º linha foi {max(matriz[1])}.')
