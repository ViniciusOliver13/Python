print('==== DESAFIO 95 ====')
gols = list()
lista = list()
posicao = total = 0
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {c+1} partida? ')))
        total += gols[c]

    jogador['gols'] = gols.copy()
    jogador['total'] = total

    lista.append(jogador.copy())

    while True:
        res = str(input('Quer continuar? [S/N] ')).upper()

        if res in 'SN':
            break
        print('Erro! Digite apenas S ou N.')

    del jogador
    gols.clear()
    total = 0

    if 'N' in res:
        break

    print('-' * 27)

print('=-' * 25)
print('cod  nome\t\tgols\t\ttotal')
print('-' * 40)

for p, c in enumerate(lista):
    print(f'{p}\t {lista[p]["nome"]:<10}{str(lista[p]["gols"]):<10}{str(lista[p]["total"]):<10}')

while True:
    print('-' * 40)
    res = int(input('Mostrar dados de qual jogador? (999 interrompe) '))

    if res == 999:
        break

    if res >= len(lista):
        print(f'Erro! Não existe jogador com o código {res}! Tente novamente.')

    elif res < len(lista):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[res]["nome"]}:')

        for p, g in enumerate(lista[res]['gols']):
            print(f'\t No jogo {p} fez {g} gols.')

print('<< VOLTE SEMPRE >>>')
