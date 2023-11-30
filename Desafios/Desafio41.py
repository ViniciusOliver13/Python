from datetime import date
print('==== DESAFIO 41 ====')
ano = int(input('Informe seu ano de nascimento: '))
categoria = date.today().year - ano
print('SUA IDADE É {}.'.format(categoria))
if categoria <= 9:
    print('SUA CATEGORIA É MIRIM!')
elif categoria <= 14:
    print('SUA CATEGORIA É INFANTIL!')
elif categoria <= 19:
    print('SUA CATEGORIA É JUNIOR!')
elif categoria == 20:
    print('SUA CATEGORIA É SÊNIOR!')
else:
    print('SUA CATEGORIA É MASTER!')
