print('==== DESAFIO 29 ====')
velo = float(input('Qual é a velocidade do carro em Km/h? '))
if velo > 80:
    print('\033[0:31mMULTADO! Você ultrapassou velocidade permitida de 80 Km/h!\nMULTA: R${:.2f}'.format((velo - 80) * 7.0))
else:
    print('\033[1:37mTenha um BOM DIA! Você está dentro da faixa de velocidade permitida!')
