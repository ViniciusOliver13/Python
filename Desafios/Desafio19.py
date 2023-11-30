import random

print('==== DESAFIO 19 ====')
print('|SORTEIO DO ALUNO|')
aluno1 = str(input('Qual é o nome do 1º? '))
aluno2 = str(input('Qual é o nome do 2º? '))
aluno3 = str(input('Qual é o nome do 3º? '))
aluno4 = str(input('Qual é o nome do 4º? '))
print('O aluno escolhindo foi\n>>> \033[1:36m{}'.format(random.choice([aluno1, aluno2, aluno3, aluno4])))