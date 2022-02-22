import random
print('Computador, escolha um número:')
num=int(random.randint(0,115))
if ((num % 2) == 0):
    print('O número escolhido (número {}) é par.'.format(num))
else:
    print('O número escolhido (número {}) é ímpar.'.format(num))
