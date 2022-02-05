n = int(input('Digite um número: '))
div = 0
for i in range(1, n+1):
    if (n % i) == 0:
        div += 1
if div == 2:
    print('O número {} possui {} divisores.  Ele É um número primo!'.format(n, div))
else:
    print('O número {} possui {} divisores. Ele NÃO é um número primo!'.format(n, div))
