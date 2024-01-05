print('==== DESAFIO 81 ====')
valores = list()
while True:
    valores.append(int(input('Informe um valor: ')))
    escolha = str(input('Deseja continuar? [S/N]')).lower()

    if 'n' in escolha:
        print('Laço finalizado!')
        break

print(f'Foram digitados {len(valores)} valores.')
print(f'Listagem decrescente dos valores: {sorted(valores, reverse= True)}')

if 5 in valores:
    print('O número 5 está na lista.')
else:
    print(f'O número 5 não está na lista.')
