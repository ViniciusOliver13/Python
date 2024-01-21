def leiaDinheiro(msg):
    while True:
        valor = str(input(f'{msg}:')).replace(",", ".").strip()

        if len(valor) > 2 and '.' in valor or valor.isnumeric():
            break

        if valor == "" or valor.isalpha():
            print(f'\033[:31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            print(f'\033[:31mERRO: "{valor}" é um preço inválido!\033[m')

    return float(valor)


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


def Menu(msg, tam):
    print('-' * tam)
    print(f'{msg}\033[m')
    print('-\033[m' * tam)
