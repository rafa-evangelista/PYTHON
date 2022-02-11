a = soma = cont = 0
while a != 999:
    a = int(input('Digite um numero (digite [999] para sair do programa):  '))
    soma += a
    cont += 1
print(f'Foram digitados {cont-1} números e a soma deles foi {soma-999}.')
