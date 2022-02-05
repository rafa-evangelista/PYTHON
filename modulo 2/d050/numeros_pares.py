from random import randint
print('')
soma = 0
cont = 0
print('Os números escolhidos foram: ', end='')
for i in range(1, 7):
    num = randint(0, 100)
    print('{}.. '.format(num), end='')
    if (num % 2) == 0:
        cont += 1
        soma += num
print('')
print('A soma dos {} números pares da lista acima foi {}.'.format(cont, soma))
print('')
