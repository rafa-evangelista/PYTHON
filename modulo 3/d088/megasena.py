from time import sleep
from random import randint

jogos = []
matriz = []

numjogos = int(input('Quantos jogos deseja fazer: '))
numdezenas = int(input('Quantas dezenas deseja jogar [entre 6 e 10]: '))
cont1 = 1
while cont1 <= numjogos:
    cont2 = 1
    while cont2 <= numdezenas:
        a = randint(1, 60)
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

for i in range(0, numjogos):
    print(f'\nJogo {i+1}: {jogos[i]}')
    sleep(1)
