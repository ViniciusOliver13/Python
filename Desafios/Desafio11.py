print('==== DESAFIO 11 ====')
print('|Quanto de tinta eu preciso?|')
alt = float(input('Qual é a altura da parede em Metros[m]? '))
lag = float(input('Qual é a largura da parede em Metros[m]? '))
a = alt * lag
print('ÁREA DA PAREDE {}m^2'.format(a))
print('Quantidade de tinta necessária para pinta-lá >>> {} litros'.format(a/2.0))