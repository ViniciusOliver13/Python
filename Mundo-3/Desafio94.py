print('==== DESAFIO 94 ====')
ficha = dict()
lista = list()
media = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

        if ficha['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')

    ficha['idade'] = int(input('Idade: '))
    media += ficha['idade']
    lista.append(ficha.copy())

    while True:
        resposta = str(input('Você quer continuar? [S/N] ')).upper()[0]

        if resposta in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')

    if resposta == 'N':
        break

media = media / len(ficha)

print('=-' * 25)
print(f'A) O grupo tem {len(lista)} pessoas.')
print(f'B) A média de idade é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')

for c in lista:
    if c['sexo'] in 'F':
        print(f'{c["nome"]} ', end='')

print(f'\nD) Lista das pessoas que estão acima da média de idade: ')

for c in lista:
    if c['idade'] >= media:
        print(f'Nome = {c["nome"]}, sexo = {c["sexo"]}, idade = {c["idade"]}')
