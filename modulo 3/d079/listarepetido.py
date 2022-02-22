números = list()
while True:
    a = int(input('Digite um número: '))
    if a in números:
        print('Valor já cadastrado.  Digite outro valor.')
    else:
        números.append(a)

    resp = ' '
    while resp not in 'SN':
        resp = str(
            input('Deseja cadastrar outro valor [S] ou [N]: ')).strip().upper()[0]
    if resp == 'N':
        break

números.sort()
print(f'Foram digitados os números {números}.')
