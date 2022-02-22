nome = str(input('Qual o seu nome completo: ')).strip()
nome_separado = nome.split()
print(' Prazer, {}!\n Esse é seu nome em letras maíusculas: {}.\n Esse é seu nome em letras minúsculas: {}.\n O seu nome possui {} letras (sem contar os espaços).\n O seu primeiro nome ({}) possui {} letras'.format(
    (nome), (nome.upper()), (nome.lower()), (len(nome) - nome.count(' ')), (nome_separado[0]), (nome.find(' '))))
