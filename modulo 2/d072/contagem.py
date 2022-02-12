num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

x = 'S'
while x == 'S':
    while True:
        extenso = int(
            input('Digite um número para exibí-lo por extenso (entre 0 e 20): '))
        if 0 <= extenso <= 20:
            break

    print(f'O número digitado foi {num[extenso]}.')

    x = 't'
    while x not in 'SN':
        x = str(input(f'Deseja continuar [S] ou [N]: ').strip() .upper()[0])
