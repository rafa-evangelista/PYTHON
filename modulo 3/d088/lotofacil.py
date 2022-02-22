from time import sleep
from random import randint

jogos = []
matriz = []
resultado = []

numjogos = int(input('Quantos jogos deseja fazer [entre 1 a 211]: '))
numdezenas = int(input('Quantas dezenas deseja jogar [entre 15 e 20]: '))
cont1 = 1
while cont1 <= numjogos:
    cont2 = 1
    while cont2 <= numdezenas:
        a = randint(0, 25)
        if cont2 == 1:
            matriz.append(a)
            cont2 += 1
        else:
            if a not in matriz:
                matriz.append(a)
                cont2 += 1
            else:
                matriz.remove(a)
                cont2 -= 1
    matriz.sort()
    jogos.append(matriz[:])
    matriz.clear()
    cont1 += 1
jogos.sort()
for i in range(0, numjogos):
    print(f'\nJogo {i+1}: {jogos[i]}')
    # sleep(1)

cont3 = 1
while cont3 <= 16:
    b = randint(0, 25)
    if cont3 == 1:
        matriz.append(b)
        cont3 += 1
    else:
        if b not in resultado:
            resultado.append(b)
            cont3 += 1
        else:
            resultado.remove(b)
            cont3 -= 1
resultado.sort()
print(f'\nAs dezenas sorteadas foram: {resultado}.')

for i in range(0, len(jogos)):
    cont4 = 0
    acertos = 0
    while cont4 <= 14:
        if resultado[cont4] in jogos[i]:
            acertos += 1
        cont4 += 1
    print(f'Jogo {i+1} = {acertos} acertos.')
