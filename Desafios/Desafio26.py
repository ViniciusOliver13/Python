print('==== DESAFIO 26 ====')
frase = str(input('Digite uma frase: ')).strip()
print('Análisando a frase "{}"'.format(frase))
print('A letra "A" apareceu {} vezes nela'.format(frase.upper().count('A')))
print('A 1º vez em que a letra "A" apareceu na posição {}'.format(frase.upper().find('A') + 1))
print('A última letra "A" apareceu na posição {}'.format(frase.upper().rfind('A') + 1))
