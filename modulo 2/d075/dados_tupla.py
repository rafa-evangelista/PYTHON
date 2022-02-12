x = (int(input('Digite o primeiro valor a ser incluído na tupla:  ')),
     int(input('Digite o segundo valor a ser incluído na tupla: ')),
     int(input('Digite o terceiro valor a ser incluído na tupla: ')),
     int(input('Digite o quarto valor a ser incluído na tupla: ')))
print(f'A tupla criada foi: {x}.')
print(f'O número 9 apareceu {x.count(9)} vez(es) na tupla.')
if 3 in x:
    print(
        f'O número 3 apareceu pela primeira vez na posição {(x.index(3))+1}.')
else:
    print('O número 3 não está na tupla.')
print('Os números pares foram: ', end='')
for i in range(0, 4):
    if x[i] % 2 == 0:
        print('[', x[i], ']', end='   ')
