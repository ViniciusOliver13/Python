from random import randint
from time import sleep
print('\033[1m==== DESAFIO 88 ====')
print('\tJOGA NA MEGA')
print('=' * 20)
palpites = int(input('O jogador quer quantos palpites? '))
jogos = []
c = num = 0
sleep(1)
print(f'-=-= SORTEANDO {palpites} JOGOS =-=-')
sleep(1)
for count in range(0, palpites):
    jogos.append(list())

    while c < 6:
        num = randint(1, 60)
        if num not in jogos[count]:
            jogos[count].append(num)
            c += 1
    c = 0
    sleep(1)
    print(f'Jogo {count + 1}º {sorted(jogos[count])}')
    sleep(1)
    if count + 1 != palpites:
        print(f'=-=' * 9)
    else:
        print(f'{" BOA SORTE!!! ":=^27}')
