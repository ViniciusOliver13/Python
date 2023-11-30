print('==== DESAFIO 34 ====')
sal = float(input('Qual é a salário desse funcionário? R$'))
if sal > 1250.0:
    print('\033[1:33mO aumento de salário é de 10%!\nNovo salário R${:.2f}'.format(sal + (sal * 10/100)))
else:
    print('\033[1:33mO aumento de salário é de 15%!\nNovo salário R${:.2f}'.format(sal + (sal * 15/100)))
