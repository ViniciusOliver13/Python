print('==== DESAFIO 12 ====')
print('|PREÇO DE UM PRODUTO|')
valor = float(input('Qual é o valor do produto? R$'))
print('Aplicando o desconto de 5% ')
print('Preço normal R${} >>> com desconto R${}'.format(valor, valor - valor * (5 / 100)))