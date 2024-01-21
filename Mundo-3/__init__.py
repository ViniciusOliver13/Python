def aumentar(n=0, p=0, f=False):
    valor = n + (n * p / 100)
    return valor if f is False else moeda(valor)


def diminuir(n=0, p=0, f=False):
    valor = n - (n * p / 100)
    return valor if f is False else moeda(valor)


def dobro(n=0, f=False):
    valor = n * 2
    return valor if f is False else moeda(valor)


def metade(n=0, f=False):
    valor = n / 2
    return valor if f is False else moeda(valor)


def moeda(form=0.0, m='R$'):
    return f'{m}{form:<.2f}'.replace('.', ',')


def resumo(p=0, au=0, re=0):
    print('\033[1m-' * 30)
    print(f'{"RESUMO DE VALOR":^30}')
    print('-' * 30)
    print(f'Preço analizado:{moeda(p):>12}')
    print(f'Dobro do preço:{dobro(p, True):>13}')
    print(f'Metade do preço:{metade(p, True):>12}')
    print(f'{au}% de aumento:{aumentar(p, au, True):>13}')
    print(f'{re}% de redução:{diminuir(p, re, True):>13}')

    return '-' * 30
