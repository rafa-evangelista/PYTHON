valor = float(input('Qual o valor do imóvel:  R$ '))
sal = float(input('Qual o seu salário:  R$ '))
tempo = int(input('Quanto tempo (anos) pretende quitar a dívida:  '))
prest = (valor / (tempo * 12))
if prest > (sal * 0.3):
    print('O empréstimo foi negado pois o valor da prestação (R$ {:.2f}) é maior que 30% do valor do salário (R$ {:.2f})'.format(
        prest, sal))
else:
    print('Parabéns! O empréstimo de R$ {:.2f} foi aprovado com parcelas mensais de R$ {:.2f} a serem pagas em {:.0f} anos!!'.format(
        valor, prest, tempo))
