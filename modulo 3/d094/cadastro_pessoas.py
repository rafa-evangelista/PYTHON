dados = {}
listafinal = []

cont = idade = somaidade = 0

while True:
    cont += 1
    dados['nome'] = str(input('Nome: ')).strip().upper()

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
        if sexo in 'MF':
            dados['sexo'] = sexo
        else:
            print('ERRO! Responda apenas M ou F')

    dados['idade'] = int(input('Idade:  '))

    listafinal.append(dados.copy())

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S] ou [N]: ')).strip().upper()
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('='*70)

print(f'\nAo todo temos {cont} pessoas cadastradas.')

for i in listafinal:
    somaidade += (i['idade'])

media = (somaidade / cont)
print(f'\nA média de idade é de {media:.1f} anos.')

print(f'\nA lista das mulheres cadastradas é: ', end='')
for i in range(0, cont):
    if listafinal[i]['sexo'] == 'F':
        print(listafinal[i]['nome'], end='    ')

print(f'\nAs pessoas com idade superior a média são: ', end='')
for i in range(0, cont):
    if listafinal[i]['idade'] > media:
        print(listafinal[i]['nome'], end='    ')
