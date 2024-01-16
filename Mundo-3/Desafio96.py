def area(lar, com):
    a = lar * com
    print(f'A área do terreno {lar:.1f}x{com:.1f} é de {a:.1f}m².')


print('==== DESAFIO 96 ====')
print('Controle de terrenos')
print('-' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
