def fatorial(n, show=False):
    """
--> Cálculo do Fatorial de um número n.
    :param n: é o número escolhido para ser feito o Fatorial.
    :param show: (opcional) Se quer ou não mostrar o processo de cálculo.
    :return: O valor do Fatorial de um número n.
    """
    valor = 1

    for c in range(n, 0, -1):
        valor *= c

        if show:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x', end=' ')

    return valor


print('==== DESAFIO 102 ====')
num = int(input('Digite um número para ver seu fatorial: '))
print('-' * 20)
print(fatorial(num, True))

