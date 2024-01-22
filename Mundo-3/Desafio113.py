def leiaInt(mens):
    while True:
        try:
            num = int(input(mens))
        except (ValueError, TypeError, NameError):
            print('\033[0:31mERRO! por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0:31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiaFloat(mens):
    while True:
        try:
            num = float(input(mens))
        except (ValueError, TypeError, NameError):
            print('\033[0:31mERRO! por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0:31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


print('==== DESAFIO 113 ====')
numInt = leiaInt('Informe um número Inteiro: ')
numFloat = leiaFloat('Informe um número Real: ')
print(f'O valor inteiro digitado foi {numInt} e o real foi {numFloat}.')
