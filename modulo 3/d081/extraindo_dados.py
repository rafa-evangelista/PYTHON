lista = []
lista1 = list()

while True:
    lista.append(int(input('Digite um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S] ou [N]: ')).strip().upper()[0]
    if resp == 'N':
        break

lista1 = lista[:]
lista1.sort(reverse=True)
print(f'Foram digitados {len(lista)} números.  Foram eles: {lista}.')
print(f'A lista digitada em ordem decrescente é: {lista1}')
if 5 in lista:
    print(f'O valor 5 aparece pela primeira vez na posição {lista.index(5)+1} da lista.')
else:
    print('O valor 5 não está na lista!!!')
