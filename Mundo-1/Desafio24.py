print('==== DESAFIO 24 ====')
nome = str(input('Digite o nome de uma cidade: ')).strip()
print('Essa cidade começa com o palavra SANTO?\n{}'.format('SANTO' in nome[:5].upper()))