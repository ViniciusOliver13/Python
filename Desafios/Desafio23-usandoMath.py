print('==== DESAFIO 23 ====')
num = int(input('Digite um número: '))
print('\033[1mO número | {} | tem...'.format(num))
mih = num//1000
print('\033[1:33mMILHAR: {}'.format(mih))
cent = (num - 1000 * mih)//100
print('\033[1:34mCENTENAS: {}'.format(cent))
deze = (num - 1000 * mih - 100 * cent)//10
print('\033[1:32mDEZENAS: {}'.format(deze))
uni = (num - 1000 * mih - 100 * cent - 10 * deze)//1
print('\033[1:36mUNIDADES: {}'.format(uni))
