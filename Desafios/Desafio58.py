from random import randint
print('==== DESAFIO 58 ====')
print('\033[:33m-=-' * 15)
print('\033[1:37:mVOU PENSAR EM UM NÚMERO ENTRE 0 E 10...')
print('\033[:33m-=-' * 15)
player = int(input('\033[mQual número você acha que pensei? '))
comp = randint(0, 10)
cont = 1
while player != comp:
    if player < comp:
        print('Mais...')
    elif player > comp:
        print('Menos...')
    player = int(input('\033[1:31mVocê errou!!\033[m Tente novamente: '))
    cont += 1
print('\033[1:36mVocê conseguiu advinhar!\nCom {} tentativas.'.format(cont))
