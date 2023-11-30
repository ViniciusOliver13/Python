from time import sleep

print('==== DESAFIO 59 ====')
test = 0
num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
while test != 5:
    print('-' * 12, '\nCALCULADORA*')
    print('-' * 12)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair')
    test = int(input('Qual opção? '))
    if test == 1:
        print('OPERAÇÃO SOMA\n{} + {} = {}'.format(num1, num2, num1 + num2))
    elif test == 2:
        print('OPERAÇÃO MULTIPLICAÇÃO\n{} + {} = {}'.format(num1, num2, num1 * num2))
    elif test == 3:
        if num1 > num2:
            print('O maior número é {}'.format(num1))
        elif num2 > num1:
            print('O maior número é {}'.format(num2))
        else:
            print('Os números são iguais.')
    elif test == 4:
        num1 = float(input('Qual é o novo 1º número? '))
        num2 = float(input('Qual é o novo 2º número? '))
    elif test == 5:
        print('Saindo.....')
        sleep(2)
    else:
        print('Opção Inválida!')
print('FIM DO PROGRAMA')
