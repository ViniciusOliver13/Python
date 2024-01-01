print('==== DESAFIO 69 ====')
teste = str()
maiores = homens = mulheres = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if 'M' in sexo:
        homens += 1
    if 'F' in sexo and idade < 20:
        mulheres += 1
    teste = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    while teste not in 'SN':
        teste = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if teste == 'N':
        break
    print('-' * 25)
print('-' * 25)
print(f'Quantidade de pessoas com mais de 18 anos: {maiores}\nQuantidade de homens {homens}\nMulheres com menos de 20 anos {mulheres} ')