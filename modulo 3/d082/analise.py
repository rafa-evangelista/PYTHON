lista = []
listapares = []
listaimpares = []

while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S] ou [N]: ')).strip().upper()[0]
    if resp == 'N':
        break

lista.sort()
print(f'Foram digitados {len(lista)} valores que ordenados ficam: {lista}.')

for i in range(0, (len(lista))):
    if lista[i] % 2 == 0:
        listapares.append(lista[i])
    else:
        listaimpares.append(lista[i])

print(f'A lista de pares é: {listapares}')
print(f'A lista de ímpares é: {listaimpares}')
