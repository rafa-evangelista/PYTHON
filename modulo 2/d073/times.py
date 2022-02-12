times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG', 'Atletico-GO',
         'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('='*100)
print('{:^100}'.format('CAMPEONATO BRASILEIRO 2021'))
print('='*100)
print(f'OS CINCO PRIMEIROS COLOCADOS FORAM: {times[0:5]}.')
print('-'*100)
print(f'OS QUATRO ÚLTIMOS COLOCADOS FORAM: {times[-4:]}')
print('-'*100)
print(
    f'OS TIMES PARTICIPANTES DO BRASILEIRÃO 2021 EM ORDEM ALFABÉTICA FORAM: {sorted(times)}')
print('-'*100)
print(
    f'O TIME DA CHAPECOENSE TERMINOU O CAMPEONATO NA {times.index("Chapecoense")+1}ª POSIÇÃO')
print('-'*100)
