from random import randint
from time import sleep

lista = []
listapar = []


def sorteio():
    print('\nSorteando 5 valores da lista:  ', end='')
    for i in range(1, 6):
        num = (randint(0, 10))
        print(f'{num}', end='   ', flush=True)
        sleep(0.8)
        lista.append(num)
    print('>>> PRONTO!')


def somapar(a):
    for v in a:
        if v % 2 == 0:
            listapar.append(v)
    soma = sum(listapar)
    print(f'\nSomando os valores pares de {a} temos {soma}.')


# Programa Principal
print('=' * 30)
print('      Sorteio de números')
print('=' * 30)

sorteio()
somapar(lista)

print('\n<<< FIM DO PROGRAMA >>>')
