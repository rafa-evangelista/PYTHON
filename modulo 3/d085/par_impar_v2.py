lista = []

for i in range(1, 8):
    lista.append(int(input(f'Digite o {i}º número:  ')))
lista.sort()
print(f'A lista formada foi {lista}.')
print(f'Os valores pares são: ', end=' ')
a = 0
while a <= 6:
    if lista[a] % 2 == 0:
        print(f'[{lista[a]}] ', end=' ')
    a += 1
print(f'\nOs valores ímpares são: ', end=' ')
a = 0
while a <= 6:
    if lista[a] % 2 != 0:
        print(f'[{lista[a]}] ', end=' ')
    a += 1
