from random import randint
from time import sleep


def sorteio(list):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        list.append(randint(1, 10))
        print(f'{list[c]} ', end='')
        sleep(0.4)
    print('Pronto!')


def somapar(valores):
    soma = 0
    for c in valores:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {valores}, temos {soma}.')


print('==== DESAFIO 100 ====')
lista = list()
sorteio(lista)
somapar(lista)
