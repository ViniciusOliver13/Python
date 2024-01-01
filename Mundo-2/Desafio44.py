print('\033[7:36m-=\033[m' * 13)
print(' \t\033[1mLOJA DO PROGRAMADOR\033[m')
print('\033[7:36m-=\033[m' * 13)
valor = float(input('PREÇO DAS COMPRAS: R$'))
op = int(input('\033[1mFORMAS DE PAGAMENTO\n[ 1 ] À VISTA DINNHEIRO/CHEQUE\n[ 2 ] À VISTA NO CARTÃO\n[ 3 ] 2x NO CARTÃO\n'
               '[ 4 ] 3x 0U MAIS VEZES NO CARTÃO\nQual método de pagamento?\033[m '))
if op == 1:
    print('FORMA DE PAGAMENTO: À VISTA DINNHEIRO/CHEQUE\nSua compra de R${:.2f} vai custar R${:.2f}'
          ''.format(valor, valor - (valor * 10 / 100)))
elif op == 2:
    print('FORMA DE PAGAMENTO: À VISTA NO CARTÃO\nSua compra de R${:.2f} vai custar R${:.2f}'
          ''.format(valor, valor - (valor * 5 / 100)))
elif op == 3:
    print('FORMA DE PAGAMENTO: 2x NO CARTÃO\nSua compra de R${:.2f} será o valor já informado com a parcela de'
          ' R${:.2f}.'.format(valor, valor / 2))
elif op == 4:
    vezes = int(input('Quantas parcelas? '))
    print('FORMA DE PAGAMENTO: 3x 0U MAIS VEZES NO CARTÃO\nSua compra de R${:.2f} será parcelada em {}x de R${} com '
          'juros.\nTotal da compra: {}'.format(valor, vezes, valor / vezes, valor + (valor * 20 / 100)))
else:
    print('COMPRA CANCELADA! TENTE NOVAMENTE!')
