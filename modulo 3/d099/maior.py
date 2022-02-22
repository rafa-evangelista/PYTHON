lista = []


def maior(*var):
    lista.append(var)
    return lista


# Programa Principal
print('=' * 50)
print('Analisador do Maior Número')
print('=' * 50)

while True:
    a = int(input('Digite um valor:  '))
    valor = maior(a)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S] ou [N]:  ')).strip().upper()[0]
    if resp == 'N':
        break

valor.sort(reverse=True)

print(f'O maior valor da lista é: {valor[0]}')
