num=int(input('Digite um número: '))
print('A tabuada do número {} é: '.format(num))
for i in range (1,11):
    print('{} x {} = {}'.format(num, i, (num * i)))
print('')
