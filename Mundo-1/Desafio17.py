import math

print('==== DESAFIO 17 ====')
cate_ad = float(input('Informe o comprimento do Cateto Adjacente: '))
cate_op = float(input('Informe o comprimento do Cateto Oposto '))
hipotenusa = math.hypot(cate_op, cate_ad)
print('O comprimeto da Hipotenusa é {:.2f}'.format(hipotenusa))