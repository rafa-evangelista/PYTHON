menor_preco = total = cont = i = 0
nome_produto = ''
continuar = 'S'
i = 0
while True:
    produto = str(input('Qual o produto deseja comprar:  ')).strip().upper()
    preco = float(input('Qual o preço do produto:  R$ '))
    if i == 0:
        menor_preco = preco
        nome_produto = produto
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_produto = produto
    i = 1

    if preco > 1000:
        cont += 1

    total += preco

    continuar = str(input('Deseja continuar [S] ou [N]: ')).strip().upper()
    if continuar == 'N':
        break
print('')
print(f'O total gasto nas compras foi de R$ {total:.2f}.')
print(f'Ao todo {cont} produtos custaram mais de R$ 1000,00.')
print(f'O nome do produto mais barato é {nome_produto}.')
