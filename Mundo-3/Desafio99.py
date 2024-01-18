from time import sleep


def maior(*num):
    cont = maior = 0
    print('=-' * 25)
    print('Analisando os valores passados...')

    for v in num:
        print(f'{v} ', end='')
        sleep(0.4)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1

    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior informado foi {maior}.')


print('==== DESAFIO 99 ====')
maior(4, 6, 3, 11, 0)
maior(8, 4, 3, 32, 44)
maior(5, 2, 10, 1, 6)
maior(1, 9, 6, 3, 2)
