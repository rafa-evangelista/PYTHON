nasc = int(input('Qual o ano do seu nascimento:  '))
ano = int(input('Qual o ano atual: '))
idade = ano - nasc
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade > 19 and idade <= 30:
    print('ADULTO')
elif idade > 30 and idade <= 40:
    print('SÊNIOR')
else:
    print('MASTER')
