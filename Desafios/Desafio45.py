from random import choice
from time import sleep
print('\033[1:35m-*' * 13, end='-\n')
print('    \033[3:35mJ  O  K  E  N  P  Ô\033[m')
print('\033[1:35m-*' * 13, end='-\n')
print('  J O G U E   C O M I G O\033[m')
print('  \033[1m[ 1 ] P E D R A\n  [ 2 ] P A P E L\n  [ 3 ] T E S O U R A')
player = int(input('QUAL É A SUA JOGADA? '))
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(jogadas)
sleep(0.5)
print('J 0')
sleep(1)
print('K E N')
sleep(1)
print('P Ô!')
sleep(0.5)
print('J O G A D A S...\nCOMPUTADOR JOGOU {} E VOCÊ '.format(comp), end='')
if 'PEDRA' in comp:
    if player == 1:
        print('PEDRA\n\033[1:37mDEU EMPATE!')
    if player == 2:
        print('PAPEL\n\033[1:33mVOCÊ GANHOU!')
    if player == 3:
        print('TESOURA\n\033[1:31mVOCÊ PERDEU!')

elif 'PAPEL' in comp:
    if player == 1:
        print('PEDRA\n\033[1:31mVOCÊ PERDEU!')
    if player == 2:
        print('PAPEL\n\033[1:37mDEU EMPATE!')
    if player == 3:
        print('TESOURA\n\033[1:33mVOCÊ GANHOU!')

elif 'TESOURA' in comp:
    if player == 1:
        print('PEDRA\n\033[1:33mVOCÊ GANHOU!')
    if player == 2:
        print('PAPEL\n\033[1:31mVOCÊ PERDEU!')
    if player == 3:
        print('TESOURA\n\033[1:37mDEU EMPATE!')
