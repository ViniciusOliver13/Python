print('==== DESAFIO 72 ====')
lista = ('zero', 'um', 'dois', 'três', 'quadro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezeseis',
         'dezessente', 'dezoito', 'dezenove', 'vinte')
test = 'S'
while test == 'S':
    escolha = int(input('Digite um número entre [0 e 20]:  '))
    if 0 <= escolha <= 20:
        print(f'O número escolhido é {lista[escolha]}.')
    else:
        print('Número inválido! ', end='')
    test = input('Deseja continuar? [S/N] ').upper()
