import random
from time import sleep

print("""
--------------------------------------------------------
                PEDRA, PAPEL OU TESOURA
--------------------------------------------------------

Computador, qual você escolhe (pedra, papel ou tesoura)
""")
sleep(1)
print('PEDRA')
sleep(1)
print('     PAPEL')
sleep(1)
print('          TESOURA')
sleep(1)

print("""
Jogador, qual você escolhe: 

[0] = pedra
[1] = papel
[2] = tesoura
""")

itens = ('pedra', 'papel', 'tesoura')
comp = int(random.randint(0, 2))
jogador = int(input('Escolha uma opção:  '))

print('==============================================')
print('O computador jogou {} e você jogou {}.'.format(itens[comp], itens[jogador]))
print('')
if comp == jogador:
    print('EMPATE, tente novamente')
elif comp == 0 and jogador == 2 or comp == 1 and jogador == 0 or comp == 2 and jogador == 1:
    print('COMPUTADOR ganhou')
else:
    print('VOCÊ ganhou')

print('==============================================')
print('')
