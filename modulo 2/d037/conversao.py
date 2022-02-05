num = int(input('Digite um número: '))
print('''Qual será a base de conversão do número {}
[1] para "binário"
[2] para "octal"
[3] para "hexadecimal"'''.format(num))
num1 = int(input('Escolha uma opção: '))

if num1 == 1:
    print('Você escolheu converter o número {} para binário. O valor é de {}.'.format(
        num, bin(num)))
elif num1 == 2:
    print('Você escolheu converter o número {} para octal. O valor é de {}'.format(
        num, oct(num)))
elif num1 == 3:
    print('Você escolheu converter o número {} para hexadecimal. O valor é de {}'.format(
        num, hex(num)))
else:
    print('Escolha uma opção válida.')
