matriz = []
cont = 0
for i in range(0, 3):
    for a in range(0, 3):
        z = int(input(f'Digite um valor para a posição {i,a}: '))
        matriz.insert(cont, z)
        cont += 1

print('='*50)

print('A matriz digitada foi:')
cont = 0
for i in range(0, 3):
    print(f'\n ')
    for a in range(0, 3):
        print(f'[{matriz[cont]}]   ', end='  ')
        cont += 1

soma = 0
for v in matriz:
    if v % 2 == 0:
        soma += v
print(f'\nA soma de todos os valores pares digitados na matriz é: {soma}.')

b = 2
soma3 = 0
for i in range(1, 10):
    if b > 9:
        break
    soma3 += matriz[b]
    b += 3
print(f'A soma de todos os valores da coluna 3 é: {soma3}.')

if matriz[3] > matriz[4] and matriz[3] > matriz[5]:
    print(f'O maior valor da segunda linha é: {matriz[3]}.')
elif matriz[4] > matriz[5] and matriz[4] > matriz[3]:
    print(f'O maior valor da segunda linha é: {matriz[4]}.')
else:
    print(f'O maior valor da segunda linha é: {matriz[5]}.')
