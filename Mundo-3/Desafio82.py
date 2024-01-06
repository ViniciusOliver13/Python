print('==== DESAFIO 82 ====')
listagem = list()
pares = list()
impares = list()

while True:
    listagem.append(int(input('Informe um número: ')))
    continuar = input('Deseja continuar? [S/N]').lower()

    if 'n' in continuar:
        print('Laço finalizado!')
        break

for pos in range(0, len(listagem) - 1):

    if listagem[pos] % 2 == 0:
        pares.append(listagem[pos])
    else:
        impares.append(listagem[pos])

print(f'Listagem de todos os números: {listagem}\nListagem dos números Pares: {pares}\n'
      f'Listagem dos números Ímpares: {impares}')
