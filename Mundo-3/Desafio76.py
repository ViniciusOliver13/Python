print('==== DESAFIO 76 ====')
tupla = ('Lápis', '5,00', 'Caderno', '15,00', 'Borracha', '3,00', 'Caneta', '7,00', 'Caderno de desenho', '12,00', 'Bloco de notas', '10,00',
         'Marca Texto', '7,50', 'Mochila', '80,00')
print('_' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_' * 40)
for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:.<32}R$ ', end=f'{tupla[i + 1]:>5}\n')
print('_' * 40)

