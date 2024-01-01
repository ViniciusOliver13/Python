print('==== DESAFIO 37 ====')
print('BASES DE CONVERÇÕES')
num = int(input('Digite um número: '))
print('Qual será a base de converção?\n1 > BINÁRIO\n2 > OCTAL\n3 > HEXADECIMAL')
base = int(input(''))
if base == 1:
    print('BASE BINÁRIA ESCOLHIDA!\nO número {} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('BASE OCTAL ESCOLHIDA!\nO número {} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('BASE HEXADECIMAL ESCOLHIDA!\nO número {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('\033[0:31mOPÇÃO INVÁLIDA!')
