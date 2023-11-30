from datetime import date
print('==== DESAFIO 54 ====')
ano = date.today().year
comp = int(0)
maiores = int(0)
menores = int(0)
for i in range(0, 7):
    idade = int(input('Informe o ano de nascimento: '))
    comp = ano - idade
    if comp >= 18:
        maiores += 1
    else:
        menores += 1
print('Total de pessoas que atingiram a maioridade: {}\nTotal de pessoas que não atingiram a maioridade: '
      '{}'.format(maiores, menores))
