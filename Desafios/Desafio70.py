print('==== DESAFIO 70 ====')
produto = barato = maisdemil = total = cont = 0
maisbarato = nome = str
teste = 'S'
while teste not in 'N':
    nome = str(input('Qual é o nome do produto? '))
    produto = float(input('Quando custa esse produto? R$'))
    total += produto
    cont += 1
    if produto > 1000:
        maisdemil += 1
    if cont == 1:
        barato = produto
        maisbarato = nome
    if produto < barato:
        barato = produto
        maisbarato = nome
    teste = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    print('=' * 25)
print(f'Total gasto R${total:.2f}\n{maisdemil} produtos custam mais de R$1000,00.\nO produto mais barato é {maisbarato} e custa R${barato:.2f}')
