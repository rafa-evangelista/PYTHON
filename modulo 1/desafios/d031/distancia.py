dist = float(input('Qual a distância da viagem (km): '))
if dist < 201:
    print('O valor a ser pago pela passagem é de R$ {:.2f}.'.format(dist * 0.5))
else:    
    print('O valor a ser pago pela passagem é de R$ {:.2f}.'.format(dist * 0.45))
