n = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = n + (10 - 1) * razao
print('Os 10 primeiros termos da PA são: ', end='')
for i in range(n, razao+ultimo, razao):
    print('{} '.format(i), end=' - ')
