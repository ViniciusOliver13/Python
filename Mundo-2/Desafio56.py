print('==== DESAFIO 56 ====')
idade = int(0)
idade_m = int(0)
maior = int(0)
m = str
f = int(0)
ge = str
nome = str('')
for i in range(1, 5):
    print('---- {}º PESSOA ----'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    idade_m = idade_m + idade
    ge = str(input('Sexo [M/F]: ')).strip()
    if idade > maior and ge == 'M':
        maior = idade
        m = nome
    if idade < 20 and ge == 'F':
        f = f + 1
print('A média de idade do grupo é de {:.1f} anos.'.format(idade_m / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, m))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(f))
