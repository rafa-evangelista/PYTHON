frase = str(input(
    'Digite uma sentença/palavra para verificar se é palíndromo: ')).strip().upper()
frase1 = (frase.replace(' ', ''))
n = len(frase1)
print('A frase digitada foi: {}.'.format(frase))
print('A frase invertida é:  ', end='')
frase2 = ''
for i in range(n-1, -1, -1):
    frase2 += (frase1[i])
print(frase2)

if frase2 == frase1:
    print('A palavra/frase digitada É um PALÍNDROMO')
else:
    print('A palavra/frase digitada NÃO é um PALÍNDROMO')
