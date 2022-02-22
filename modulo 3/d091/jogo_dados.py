from random import randint
from time import sleep
from operator import itemgetter

ranking = {}
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)}

print('Valores Sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'\n{i+1}º lugar: {v[0]} com {v[1]}.')
