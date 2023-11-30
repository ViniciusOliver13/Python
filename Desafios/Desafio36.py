print('==== DESAFIO 35 ====')
print('EMPRÉSTIMO BANCÁRIO')
casa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Planeja pagar em quantos anos? '))
parcela = casa/(12 * anos)
print('RESPOSTA DO PEDIDO...')
if parcela > (sal * 30 / 100):
    print('Infelizmente você não pode efetuar o empréstimo. Valor da parcela R${:.2f}.\nTente novamente!'.format(parcela))
elif parcela <= (sal * 30 / 100):
    print('Boa notícia! Você pode efetuar o empréstimo!\nValor parcela mensal: R${:.2f}.'.format(parcela))
