valor1 = float(input('Digite o valor do produto: R$ '))
print('Qual a forma de pagamento: ')
print('[1] = a vista em dinheiro ou cheque (10% de desconto)')
print('[2] = a vista no cartão de crédito (5% de desconto)')
print('[3] = parcelamento em até 2x no cartão de crédito (pagamento sem juros)')
print('[4] = parcelamento em 3x ou mais no cartão de crédito (20% de juros)')
pagamento = int(input('Escolha uma opção: '))
if pagamento == 1:
    valor1 = valor1*0.9
    print('O novo valor do produto é R$ {:.2f}.'.format(valor1))
elif pagamento == 2:
    valor1 = valor1*0.95
    print('O novo valor do produto é R$ {:.2f}.'.format(valor1))
elif pagamento == 3:
    print('O produto não teve desconto. Valor de R$ {:.2f} parcelado em 2x sem juros de R$ {:.2f}.'.format(
        valor1, (valor1/2)))
elif pagamento == 4:
    prestacao = int(input('Deseja parcelar em quantas vezes (acima de 2x): '))
    valor1 = valor1*1.2
    print('O novo valor do produto é R$ {:.2f}, parcelado em {:.0f}x de R$ {:.2f}.'.format(
        valor1, prestacao, (valor1/prestacao)))
