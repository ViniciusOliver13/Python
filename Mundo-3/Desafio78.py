print('==== DESAFIO 78 ====')
valores = list()
for i in range(0, 4):
    valores.append(int(input('Digite um valor: ')))
print(f'{valores}\nMaior valor foi {max(valores)} nas posições ', end='')
for c in range(0, 4):
    if valores[c] == max(valores):
        print(f'{[c]}...', end='')
print(f'\nMenor valor foi {min(valores)} nas posições ', end='')
for c in range(0, 4):
    if valores[c] == min(valores):
        print(f'{[c]}...', end='')
