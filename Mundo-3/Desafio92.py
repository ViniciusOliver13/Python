from datetime import date
print('==== DESAFIO 92 ====')
pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contração'] = int(input('Ano de contração: '))
    pessoa['salário'] = float(input('Qual foi o salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contração'] + pessoa['idade'] + 35) - date.today().year
print('=-' * 20)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}.')
