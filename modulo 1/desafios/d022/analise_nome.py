nome = input('Qual o seu nome completo: ')
nome_separado = nome.split
tamanho = len(nome_separado, [:])

print(' Prazer, {}!\n Esse é seu nome em letras maíusculas: {}.\n Esse é seu nome em letras minúsculas: {}.\n O seu nome possui {} letras (sem contar os espaços).\n Seu primeiro nome ({})possui {} letras.'.format(
    nome, (nome.upper), (nome.lower), tamanho))
