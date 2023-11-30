print('==== DESAFIO 33 ====')
n1 = int(input('\033[1mDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2           #VERIFICANDO O MENOR NÚMERO
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2          #VERIFICANDO O MAIOR NÚMERO
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[0:36mO MAIOR NÚMERO É {}\033[m\n\033[0:35mO MENOR NÚMERO É {}'.format(maior, menor))
