from utilidadesCeV import moeda, dado
print('==== DESAFIO 111-112 ====')
p = dado.leiaDinheiro('Digite o preço: R$')
print(moeda.resumo(p, 35, 22))
