print('==== DESAFIO 83 ====')
expressao = str(input('Digite uma expresssão: '))
lista = list()
for simb in expressao:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')