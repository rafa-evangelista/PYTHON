lista = []
alunos = []
cont = 0

print('='*50)
print(f'PROGRAMA DE NOTA ESCOLAR')
print('='*50)

while True:
    alunos.append(str(input('Nome: ')).strip().upper())
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    alunos.append((alunos[1] + alunos[2])/2)

    lista.append(alunos[:])
    alunos.clear()

    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S] ou [N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('=' * 50)
print(f'BOLETIM ESCOLAR:')
print('=' * 50)
print('Nº         NOME         MÉDIA          ')

for i in range(0, cont):
    print(i, end='          ')
    print((lista[i][0]), end='         ')
    print((lista[i][3]))

while True:
    a = int(input('Deseja mostrar as notas de qual aluno [999 para sair]? '))
    if a == 999:
        break
    print(f'Notas de {lista[a][0]} são {lista[a][1]} e {lista[a][2]}.')
