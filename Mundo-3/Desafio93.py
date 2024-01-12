print('==== DESAFIO 93 ====')
jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {c+1} partida? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=-' * 25)
print(jogador)
print('=-' * 25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 25)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for p, v in enumerate(jogador['gols']):
    print(f'    => Na partida {p+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]}.')
