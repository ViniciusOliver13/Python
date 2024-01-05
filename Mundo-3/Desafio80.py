print('==== DESAFIO 80 ====')
lista = list()
for i in range(0, 5):
    num = int(input('Digite um valor: '))

    if i == 0 or num > max(lista):
        print(f'Valor adicionado no fim da lista!')
        lista.append(num)
    elif num < min(lista):
        print(f'Valor adicionado no inicio da lista!')
        lista.insert(0, num)
    else:
        for pos in range(len(lista) - 1, 0, -1):
            if lista[pos - 1] < num:
                lista.insert(pos, num)
                print(f'Valor adicionado na posição {pos + 1}!')
                break
print(f'{lista}')
