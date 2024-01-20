#   ==== DESAFIO 107-108 ====

def aumentar(n=0, p=0):
    return n + (n * p / 100)


def diminuir(n=0, p=0):
    return n - (n * p / 100)


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(p=0, m='R$'):
    return f'{m}{p:<.2f}'.replace('.', ',')
