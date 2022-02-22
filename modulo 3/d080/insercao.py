lista = []
for i in range(0, 11):
    num = int(input('Digite um número: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Valor {num} foi inserido no final da lista.')
    else:
        pos = 0
        while pos <= len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor {num} foi inserido na posição {pos} da lista.')
                break
            pos += 1

print('='*50)
print(f'Os valores digitados em ordem foram {lista}')
