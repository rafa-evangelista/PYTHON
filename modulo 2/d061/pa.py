termo_1 = int(input('Digite o primeiro termo da PA:  '))
razao = int(input('Digite a razão da PA:  '))
print('Os 10 primeiros termos da PA são:  ', end='')
i = 1
while i <= 10:
    print(f'[{termo_1}]', end='  ')
    termo_1 += razao
    i += 1
