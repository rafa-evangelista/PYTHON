sexo = str(input('Informe o sexo: [M] ou [F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos.  Por favor, informe seu sexo:  ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
