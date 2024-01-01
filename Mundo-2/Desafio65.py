print('==== DESAFIO 65 ====')
num = cont = maior = menor = soma = 0
test = str
while test != 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    test = str(input('Você quer continuar? [S/N] ')).upper()
print('A média entre os números foi {:.2f}\nO maior número foi {}\nO menor número foi {}'.format(soma / cont, maior, menor))
