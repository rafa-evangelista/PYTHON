sair = str('N')
soma = cont = maior = menor = i = 0
while sair == 'N':
    a = int(input('Digite um número: '))
    soma += a
    cont += 1
    if i == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
    i = 1
    sair = str(input('Deseja sair do programa? Digite [s] ou [n]:  ')).strip() .upper() [0]
print(f'A média dos números digitados foi {(soma/cont):.2f}. O maior número digitado foi {maior} e o menor número digitado foi {menor}')
