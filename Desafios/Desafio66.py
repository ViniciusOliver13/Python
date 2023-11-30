print('==== DESAFIO 66 ====')
num = int(input('Digite um número: '))
soma = cont = 0
while True:
    if num == 999:
        break
    soma += num
    cont += 1
    num = int(input('Digite um número: '))
print(f'Foram digitados {cont} números e a soma foi {soma}.')
