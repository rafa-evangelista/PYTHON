n = int(input('Quantos termos da PA deseja exibir:  '))
termo_1 = int(input('Digite o primeiro termo da PA:  '))
razao = int(input('Digite a razão da PA:  '))
print(f'Os {n} primeiros termos da PA são: ', end='')
i = 1
while i <= n:
    print(f'[{termo_1}]', end='  ')
    termo_1 += razao
    i+=1 
print('')
print('')
continuar=str(input('Deseja continuar a exibir os termos da PA? [S] ou [N]:  ')).strip().upper() [0]
while continuar == 'S':
    termos_novos = int(input('Quantos termos novos deseja exibir:  '))
    print('Os novos termos da PA são:  ', end='')
    i=1
    while i <= termos_novos:
        print(f'[{termo_1}]', end='  ')
        termo_1 += razao
        i+=1          
    print('')
    print('')
    continuar=str(input('Deseja continuar a exibir os termos da PA? [S] ou [N]:  ')).strip().upper() [0]
print('FIM DA EXECUÇÃO DO PROGRAMA!')
