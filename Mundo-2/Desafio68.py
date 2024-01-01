from random import randint
print('==== DESAFIO 68 ====')
print('-=' * 15)
print('  VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
cont = 0
teste = False
while True:
    while not teste:
        comp = randint(0, 10)
        print(comp)
        num = int(input('Diga um valor: '))
        jogar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        total = num + comp
        if total % 2 == 0:
            print(f'Você jogou {num} e computador {comp}. Total de {num + comp} DEU PAR')
        else:
            print(f'Você jogou {num} e computador {comp}. Total de {num + comp} DEU ÍMPAR')
        if jogar == 'P':
            if total % 2 == 0:
                print('Você Venceu!!')
                cont += 1
            else:
                print('Você perdeu!')
                if cont > 0:
                    teste = True
        elif jogar == 'I':
            if total % 2 == 0:
                print('Você perdeu!')
                if cont > 0:
                    teste = True
            else:
                print('Você Venceu!!')
                cont += 1
    break
print(f'Partida finalizada com {cont} vitórias consecutivas')
