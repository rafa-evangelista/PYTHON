jogadores = {}
geral = []
gols = []

print('='*70)
print('                        ESTATÍSTICA DE JOGADOR')
print(f'='*70)

while True:
    jogadores['nome'] = str(input('Qual o nome do jogador:  ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogadores["nome"]} jogou?  '))

    if partidas != 0:
        for i in range(0, partidas):
            gols.append(
                int(input(f'     Quantos gols {jogadores["nome"]} fez na partida {i+1}: ')))

        jogadores['listagols'] = gols[:]
        jogadores['totalgols'] = sum(jogadores['listagols'])
        jogadores['partidas'] = partidas
        gols.clear()

        geral.append(jogadores.copy())

    else:
        print(f'O jogador {jogadores["nome"]} ainda não estreou no seu Clube.')

    resp = ' '
    while resp not in 'SN':
        resp = str(
            input('Deseja incluir mais um jogador [S] ou [N]?  ')).strip().upper()[0]
    if resp == 'N':
        break

print('=' * 70)
print('Código            Nome           Gols            Total            ')
print('=' * 70)

for i in range(0, len(geral)):
    print(f'{  i:<15}', end='   ')
    print(f'{geral[i]["nome"]:<15}', end='')
    print(f'{geral[i]["listagols"]}', end='')
    print(f'{geral[i]["totalgols"]:^28}')
print('=' * 70)

while True:
    analise = int(
        input('Deseja mostrar dados de qual jogador [999 para sair]:  '))
    if analise == 999:
        break
    elif analise >= len(geral):
        print(
            f'Código informado ({analise}) não está presente na lista. Tente novamente.')
    else:
        print(f'--- LEVANTAMENTO DO JOGADOR {geral[analise]["nome"]}:')
        for i, g in enumerate(geral[analise]["listagols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
print('-' * 70)

print('<<< VOLTE SEMPRE >>>')
