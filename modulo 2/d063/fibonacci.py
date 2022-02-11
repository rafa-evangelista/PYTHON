n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar:  '))
a = c = 0
b = i = 1
print(f'Os {n} primeiros termos da Seqüência de Fibonacci são: ', end='')
print(a, end='   ')
while i < n:
    print(b, end='   ')
    c = b
    b = b + a
    a = c
    i += 1
