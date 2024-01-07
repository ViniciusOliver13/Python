print('==== DESAFIO 84 ====')
pessoas = []
dados = []
menor = maior = count = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso[Kg]: ')))
    pessoas.append(dados[:])
    dados.clear()
    escolha = input('Você quer continuar? [S/N]').lower()

    if count == 0:
        maior = menor = pessoas[0][1]

    if maior < pessoas[count][1]:
        maior = pessoas[count][1]

    if menor > pessoas[count][1]:
        menor = pessoas[count][1]

    if 'n' in escolha:
        break

    count += 1

print('=-' * 25)
print(f'Foram cadastradas {len(pessoas)}.')
print(f'Pessoas mais pesadas foi {maior}Kg: ', end='')

for c in range(0, len(pessoas)):
    if pessoas[c][1] == maior:
        print(f'[{pessoas[c][0]}] ', end='')

print(f'\nPessoas mais leves foi {menor}Kg: ', end='')

for c in range(0, len(pessoas)):
    if pessoas[c][1] == menor:
        print(f'[{pessoas[c][0]}] ', end='')
