dados = []
dadosfinal = []
leve = pesada = 0

while True:
    dados.append(str(input('Qual o nome da pessoa: ').strip().upper()))
    dados.append(float(input('Qual o peso da pessoa (kg):  ')))

    if len(dadosfinal) == 0:
        leve = pesada = dados[1]
    else:
        if dados[1] > pesada:
            pesada = dados[1]
        if dados[1] < leve:
            leve = dados[1]

    dadosfinal.append(dados[:])
    dados.clear()

    resp = ' '
    while resp not in 'SN':
        resp = str(
            input('Deseja continuar com o cadastro [S] ou [N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastradas {len(dadosfinal)} pessoas.')
print(f'O maior peso foi de {pesada}kg. Pertencente a  ', end='')
for p in dadosfinal:
    if p[1] == pesada:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {leve}kg. Pertencente a  ', end='')
for p in dadosfinal:
    if p[1] == leve:
        print(f'[{p[0]}]')
