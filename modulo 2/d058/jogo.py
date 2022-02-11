from random import randint
from time import sleep

print('Computador, pense em um número:  ')
print('Estou pensando ...')
sleep(3)
print('...  PRONTO, JÁ ESCOLHI!!!  SUA VEZ! TENTE ADIVINHAR O NÚMERO QUE ESCOLHI!')
comp = randint(0, 10)
num = int(input('Escolha um número:  '))
i = 1
while num != comp:
    i += +1
    print('Número errado. TENTE NOVAMENTE!')
    if num < comp:
        print('O número que escolhi é maior!')
    else:
        print('O número que escolhi é menor!')
    num = int(input('Escolha novamente um número:  '))
print('Parabéns! Você acertou o número escolhido pelo computador ({}).  Para isso foi preciso {} tentativa(s).'.format(comp, i))
