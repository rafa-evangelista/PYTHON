import datetime
anonasc = int(input('Qual o ano do seu nascimento (formato "aaaa"):  '))
anoatual = datetime.date.today().year
if (anoatual - anonasc) == 18:
    print('Está na hora de se alistar')
elif (anoatual - anonasc) < 18:
    print('Ainda não está na hora de se alistar. Faltam {} ano(s)'.format(
        18 - (anoatual - anonasc)))
else:
    print('Já passou da hora de se alistar. Você está {} ano(s) atrasado(s).'.format(
        (anoatual - anonasc) - 18))
