print('==== DESAFIO 39 ====')
print('ALISTAMENTO MILITAR')
ano = int(input('Informe seu ano de nascimeto: '))
anali = 2023 - ano
if anali < 18 and ano > 0:
    print('Você ainda vai se alistar ao SERVIÇO MILITAR.\nFalta ainda {} anos para o seu alistamento.\nSeu alistamento será'
          ' em {}.'.format(18 - anali, ano + 18))
elif anali == 18 and ano > 0:
    print('Já é hora de se alistar! Faça o alistamento Online ou na Junta Militar mais próxima!')
elif anali > 18 and ano > 0:
    print('Você passou do tempo do alistamento!\nVocê já deveria ter se alistado há {} anos.\nSeu alistamento deveria'
          ' ser feito em {}.'.format(anali - 18, ano + 18))
else:
    print('Erro....')
