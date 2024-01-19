def notas(*n_notas, sit=False):
    """
    --> Função para analizar várias notas e retornar valores como: maior nota, menor nota, média,
    situação (opcional).

    :param n_notas: uma ou 'n' notas de alunos.
    :param sit: valor opcional, indicando se deve ou não adicionar o campo 'situação'.
    :return: dicionário várias informações sobre o desempenho da turma.
    """

    ficha = {'total': len(n_notas), 'maior': max(n_notas),
             'menor': min(n_notas), 'media': sum(n_notas) / len(n_notas)}

    if sit:
        if ficha['media'] >= 7.0:
            situacao = "BOA"
        elif ficha['media'] >= 5.0:
            situacao = "RAZOÁVEL"
        else:
            situacao = "RUIM"
        ficha['situação'] = situacao[:]

    return ficha


print('==== DESAFIO 105 ====')
print('-' * 40)
resp = notas(2, 4, 6, 10, 4, sit=True)
print(resp)
