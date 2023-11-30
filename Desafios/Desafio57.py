print('==== DESAFIO 57 ====')
genero = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while genero not in 'MF':
    genero = str(input('Digite novamente o seu sexo [M/F]: ')).strip().upper()[0]
print('Fim da pergunta!')
