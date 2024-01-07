print('==== DESAFIO 85 ====')
numeros = [[], []]
for count in range(0, 7):
    num = int(input(f'Digite {count + 1}º número: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('=-' * 20)
print(f'Foram digitados {len(numeros[0])} números Pares: {sorted(numeros[0])}')
print(f'Foram digitados {len(numeros[1])} números Ímpares: {sorted(numeros[1])}')
