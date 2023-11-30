print('==== DESAFIO 61 E 62 ====')
num = int(input('Qual é o primeiro termo da PA? '))  # num, term + r, r
r = int(input('Qual é a razão? '))
term = num + (10 - 1) * r
teste = 1
cont = 0
while teste != 0:
    while num != term + r:
        print('{} -> '.format(num), end='')
        num += r
        cont += 1
    teste = int(input('ACABOU\nDeseja ver quantos termos a mais? '))
    term += teste * r
print('Progressão finalizada com {} termos mostrados.'.format(cont))
