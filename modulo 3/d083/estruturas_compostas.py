
a = str(input('Digite a expressão:  '))
abre = a.count('(')
fecha = a.count(')')
if abre == fecha:
    print(f'A exoressão [{a}] é válida.')
else:
    print(f'A exoressão [{a}] está errada.')
