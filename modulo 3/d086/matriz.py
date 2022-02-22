matriz = []
cont = 0
for i in range(0, 3):
    for a in range(0, 3):
        z = int(input(f'Digite um valor para a posição {i,a}: '))
        matriz.insert(cont, z)
        cont += 1

print('='*50)

print('A matriz digitada foi:')
cont = 0
for i in range(0, 3):
    print(f'\n ')
    for a in range(0, 3):
        print(f'[{matriz[cont]:^5}]   ', end='  ')
        cont += 1
