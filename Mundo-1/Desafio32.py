from datetime import date

print('==== DESAFIO 32 ====')
ano = int(input('\033[1;mDigite um ano qualquer ou coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[4mO ano {} é BISSEXTO!'.format(ano))
else:
    print('\033[4mO ano {} NÃO é BISSEXTO!'.format(ano))
