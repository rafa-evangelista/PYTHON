import random
print('Computador, pense em um número...')
num=int(random.randint(0,10))
num2=int(input('Tente adivinhar o número entre "0" e "10" que o computador escolheu: '))
if num2 == num:
    print('Parabéns, você adivinhou o número pensado pelo computador (número {})'.format(num))
else:
    print('Você não adivinhou o número escolhido pelo computador (número {}).  Tente novamente!'.format(num))
