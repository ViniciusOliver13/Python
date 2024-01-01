print('==== DESAFIO 63 ====')
print('   | FIBONACCI |')
n1 = 0
n2 = 1
while n1 < 1000:
    print(n1, end=' -> ')
    n2 += n1
    print(n2, end=' -> ')
    n1 += n2
print('FIM')