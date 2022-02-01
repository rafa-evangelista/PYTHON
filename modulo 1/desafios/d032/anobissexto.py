ano = int(input('Digite o ano a ser pesquisado (formato "aaaa"): '))
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print('O ano de {} É bissexto.'.format(ano))
else: 
    print('O ano de {} NÃO É um ano bissexto.'.format(ano))
    