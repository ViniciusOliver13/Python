from time import sleep


def ajuda(comando):
    sleep(0.5)
    print('\033[1:44m~' * (36 + len(comando)))
    print(f'  Acessando o manual do comando "{comando}"')
    print('~' * (36 + len(comando)))
    sleep(1)

    return help(comando)


print('==== DESAFIO 106 ====')

while True:

    print('\033[m\033[3:33:40:1m~' * 29)
    print('   SISTEMA DE AJUDA PyHELP')
    print('~' * 29)

    funcao = str(input('\033[m\033[1:38mFunção ou Biblioteca >\033[m ')).lower()

    if 'fim' in funcao:
        sleep(0.4)
        print('\033[1::41m~' * 11)
        print(' ATÉ LOGO! ')
        print('~' * 11)
        sleep(0.4)

        break

    resp = ajuda(funcao)
