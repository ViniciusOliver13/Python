print('==== DESAFIO 71 ====')
print(' CAIXA ELETRÔNICO')
num = int(input('Quanto você quer sacar? R$'))
nota50 = nota20 = nota10 = nota1 = cont = 0
while num != 0:
    cont += 1
    if cont == 1:
        nota50 = num // 50
        num -= nota50 * 50
    elif cont == 2:
        nota20 = num // 20
        num -= nota20 * 20
    elif cont == 3:
        nota10 = num // 10
        num -= nota10 * 10
    else:
        nota1 = num // 1
        num -= nota1 * 1
print(f'Nota de 50: {nota50}\nNota de 20: {nota20}\nNota de 10: {nota10}\nNota de 1: {nota1}')
