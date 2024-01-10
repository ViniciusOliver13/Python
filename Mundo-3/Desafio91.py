from random import randint
from operator import itemgetter
from time import sleep
print('==== DESAFIO 91 ====')
players = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteiados:')
for k, v in players.items():
    print(f'    O {k} tirou {v}.')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

print('== RANKKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
