print('==== DESAFIO 77 ====')
palavras = ('ABACATE', 'VACA', 'CAJU', 'UVA')
for i in palavras:
    print(f'\nA palavra {i} tem vogais ', end='')
    for letras in i:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')