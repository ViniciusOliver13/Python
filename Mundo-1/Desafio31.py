print('==== DESAFIO 31 ====')
km = float(input('Qual é a distância da viagem? '))
if km <= 200.0:
    print('O custo da viagem por Km é R$0.50:\nTotal a pagar: \033[:33mR${:.2f}'.format(km * 0.50))
else:
    print('O custo da viagem por Km é R$0.45:\nTotal a pagar: \033[:33mR${:.2f}'.format(km * 0.45))
