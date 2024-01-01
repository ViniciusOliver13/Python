import math

print('==== DESAFIO 18 ====')
graus = int(input('Digite um Ângulo: '))
angulo = math.radians(graus)
seno = math.sin(angulo)
cosse = math.cos(angulo)
tange = math.tan(angulo)
print('\033[4mVALORES ENCONTRADOS PARA {}º\nSENO >>> {}\nCOSSENO >>> {}\nTANGENTE >>> {}'.format(graus, seno, cosse, tange))
