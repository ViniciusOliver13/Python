print('==== DESAFIO 40 ====')
nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2 nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('\033[1:31mALUNO REPROVADO!\nMÉDIA: {:.1f}'.format(media))
elif media >= 5 and media < 7:
    print('\033[1:33mALUNO VAI PARA RECUPERAÇÃO!\nMÉDIA: {:.1f}'.format(media))
else:
    print('\033[1:36mPARABÉNS! ALUNO APROVADO!\nMÉDIA: {:.1f}'.format(media))
