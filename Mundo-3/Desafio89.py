print('==== DESAFIO 89 ====')
turma = list()
count = 0
while True:
    turma.append(list())
    turma[count].append(str(input('Nome: ')))
    turma[count].append(list())
    turma[count][1].append(float(input('1º Nota: ')))
    turma[count][1].append(float(input('2º Nota: ')))

    escolha = str(input('Deseja continuar? [S/N] ')).lower()
    count += 1

    if 'n' in escolha:
        break

print('=-' * 20)
print(f'No.\t   {"NOME":<13} MÉDIA')
print('-' * 26)
for alunos in range(0, len(turma)):
    print(f'{alunos:<5}  {turma[alunos][0]:<10}{((turma[alunos][1][0] + turma[alunos][1][1]) / 2):>8.1f}')

while escolha != 999:
    print('-' * 26)
    escolha = int(input('Mostrar notas de qual aluno? {999} interrompe: '))

    if escolha <= len(turma) - 1:
        print(f'Notas de {turma[escolha][0]} são: {turma[escolha][1]}')
    else:
        print('Número inválido!')
print('\nENCERRANDO...\n<<< VOLTE SEMPRE >>>')
