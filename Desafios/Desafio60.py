print('==== DESAFIO 60 ====')
num = int(input('Digite um número e veja seu fatorial: '))
n = num
print('{}! = {} '.format(num, num), end='')
while n > 1:
    n -= 1
    num = num * n
    print(''.format(n), end='x {} '.format(n))
print('= {}'.format(num))
