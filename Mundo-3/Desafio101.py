def voto(ano):
    from datetime import date
    global nasc

    nasc = ano = date.today().year - ano

    if ano < 16:
        return f'Com {nasc} anos: NÃO VOTA'
    elif 16 <= ano < 18 or ano > 65:
        return f'Com {nasc} anos: VOTO OPCIONAL'
    else:
        return f'Com {nasc} anos: VOTO OBRIGATÓRIO'


print('==== DESAFIO 101 ====')
print('-' * 20)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
