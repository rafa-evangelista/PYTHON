vel=float(input('Qual a velocidade do carro:  '))
valor=float((vel - 80)*7)
if vel > 80:
    print('Você estava com velocidade superior a 80 km/h e foi multado.  A multa a ser paga tem o valor de R$ {:.2f}.'.format(valor))
else:
    print('Parabéns! Você estava com a velocidade dentro dos limites.')
