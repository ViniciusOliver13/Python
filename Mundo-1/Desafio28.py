from random import randint
print('==== DESAFIO 28 ====')
print('\033[:33m-=-' * 15)
print('\033[1:37:mVOU PENSAR EM UM NÚMERO ENTRE 0 E 5...')
print('\033[:33m-=-' * 15)
player = int(input('\033[mDiga um número entre 0 e 5: '))
comput = randint(0, 5)
if player == comput:
    print('\033[1:33mVocê VENCEU a advinhação!')
else:
    print('\033[1:31mVocê PERDEU a advinhação!')
print('Número do computador {}\nSeu número {}'.format(comput, player))