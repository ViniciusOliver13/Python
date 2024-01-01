print('==== DESAFIO 53 ====')
nome = str(input('Digite uma frase: ')).strip()
tet = ''.join(nome.split())
final = str('')
for c in range(len(tet), 0, -1):
    final = final + tet[c-1]
if final == tet:
    print('A frase "{}"\n\033[1:36mÉ UM PALÍNDROMO!'.format(nome))
else:
    print('A frase "{}"\n\033[1:31mNÃO É UM PALÍNDROMO!'.format(nome))
