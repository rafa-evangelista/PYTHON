jogador = {}
totpartida = []

print('='*70)
print('                        ESTATÍSTICA DE JOGADOR')
print(f'='*70)

jogador['nome'] = str(input('Qual o nome do jogador:  ')).strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?  '))

if partidas != 0:
    for i in range(0, partidas):
        totpartida.append(
            int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: ')))
        jogador['golpartida'] = totpartida
        jogador['total'] = sum(jogador['golpartida'])

    print('='*70)
    print(f'{jogador}')

    print('='*70)
    for k, v in jogador.items():
        print(f'O campo {k} tem valor de {v}.')

    print('='*70)
    print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
    for i, v in enumerate(jogador["golpartida"]):
        print(f'=> Na partida {i+1}, fez {v} gols.')
    print(f'Foi um total de {jogador["total"]} gols.')
else:
    print(f'O jogador {jogador["nome"]} ainda não estreou no seu Clube.')
