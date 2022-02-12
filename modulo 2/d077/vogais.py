listagem = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
            'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in range(0, len(listagem)):
    print(f'\nNa palavra {(listagem[i])} temos as seguintes vogais:  ', end='')
    for letra in (listagem[i]):
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
print('')
print('=' * 50)
