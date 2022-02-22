from random import randint
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (randint(0, 20))
print('A matriz randomizada foi: ')
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'[{matriz [l] [c]:^5}]', end='    ')

soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print(f'\nA soma dos números pares da matriz é {soma}.')

soma3 = 0
for l in range(0, 3):
    soma3 += (matriz[l][2])
print(f'A soma dos números da terceira coluna é {soma3}.')

maior = 0
for c in range(0, 3):
    if (matriz[1][c]) > maior:
        maior = (matriz[1][c])
print(f'O maior valor da segunda linha é {maior}.')
