lista = []
for i in range(1, 6):
    lista.append(int(input(f'Digite um número para a posição {i}:  ')))
minimo = (min(lista))
maximo = (max(lista))
print(f'A lista digitada foi: {lista}.')
print(
    f'O menor valor da lista é {minimo} e ele está na posição {lista.index(minimo)+1}...')
print(
    f'O maior valor da lista é {maximo} e ele está na posição {lista.index(maximo)+1}...')
