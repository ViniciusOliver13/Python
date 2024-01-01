print('==== DESAFIO 27 ====')
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('1º nome = {}\nÚltimo nome = {}'.format(lista[0], lista[len(lista) - 1]))
