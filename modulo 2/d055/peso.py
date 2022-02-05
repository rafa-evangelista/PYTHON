maior=0
menor=0
for i in range(1,6):
    peso=float(input('Digite o peso da {}ª pessoa (kg):  '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print('Ao todo {} pessoas foram pesadas.  O maior peso foi {}kg e o menor peso foi {}kg.'.format(i, maior, menor))
