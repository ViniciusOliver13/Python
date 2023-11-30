print('==== DESAFIO 43 ====')
print('\t   \033[1:36mIMC\033[m')
peso = float(input('Qual é a sua massa? '))
alt = float(input('Qual é a sua altura? '))
imc = peso / (alt ** 2)
print('SEU IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('SEU STATUS É \033[4:33mABAIXO DO PESO!')
elif imc < 25:
    print('SEU STATUS É \033[4:33mPESO IDEAL!')
elif imc < 30:
    print('SEU STATUS É \033[4:33mSOBREPESO!')
elif imc < 40:
    print('SEU STATUS É \033[4:33mOBESIDADE!')
elif imc >= 40:
    print('SEU STATUS É \033[4:33mOBESIDADE MÓRBIDA!')
else:
    print('ALGO DEU ERRADO!')
