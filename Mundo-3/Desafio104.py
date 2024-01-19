def leiaInt():
    while True:
        num = str(input('Informe um número inteiro: ')).strip()

        if num.isnumeric():
            return num
        else:
            print('\033[0:31mERRO! Digite um número inteiro válido.\033[m')


print('==== DESAFIO 104 ====')
n = leiaInt()
print(f'Você acabou de digitar o número {n}.')
