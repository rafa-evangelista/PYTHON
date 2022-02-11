num1 = int(input('Digite o primeiro número:  '))
num2 = int(input('Digite o segundo número:  '))
i = 0
while i != 5:
    print("""
    Escolha uma opção abaixo para trabalhar com os números:
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DO PROGRAMA """)
    i = int(input('Digite a opção: '))
    if i == 1:
        print(f'A soma é {num1 + num2}')
    elif i == 2:
        print(f'A multiplicação é {num1 * num2}')
    elif i == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}')
        else:
            print(f'O número {num2} é maior que o número {num1}')
    elif i == 4:
        num1 = int(input('Digite o primeiro número:  '))
        num2 = int(input('Digite o segundo número:  '))
