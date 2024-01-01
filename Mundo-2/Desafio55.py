print('==== DESAFIO 55 ====')
maior = float(0)
menor = float(0)
for i in range(0, 5):
    peso = float(input('Informe o peso: Kg '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso foi {}Kg\nO MENOR peso foi {}Kg'.format(maior, menor))
