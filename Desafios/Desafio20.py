import random

print('==== DESAFIO 20 ====')
alun1 = str(input('Digite o nome do 1º: '))
alun2 = str(input('Digite o nome do 2º: '))
alun3 = str(input('Digite o nome do 3º: '))
alun4 = str(input('Digite o nome do 4º: '))
lista = alun4, alun3, alun2, alun1
ordem = random.sample([alun1, alun2, alun3, alun4], k=4)
print('A ordem sorteiada foi...\n>> {}'.format(ordem))