print('==== DESAFIO 42 ====')
l1 = int(input('\033[1mDigite a medida da 1º reta: '))
l2 = int(input('Digite a medida da 2º reta: '))
l3 = int(input('Digite a medida da 3º reta: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[1:33mVOCÊ PODE FORMAR UM TRIÂNGULO ', end='')
    if l1 == l2 == l3:
        print('DO TIPO EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('DO TIPO ESCALENO!')
    else:
        print('DO TIPO ISÓSCELES!')
else:
    print('\033[1:31mVOCÊ NÃO PODE FORMAR UM TRIÂNGULO!')
