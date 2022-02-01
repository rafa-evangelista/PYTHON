sal=float(input('Qual o salário do funcionário: R$ '))
if sal > 1250:
    print('O novo salário do funcionário será de R$ {:.2f}.'.format(sal * 1.1))
else:
    print('O novo salário do funcionário será de R$ {:.2f}.'.format(sal * 1.15))