cidade = str(input('Digite a Cidade onde você nasceu: ')).strip().title()
print(cidade)
print('A palavra "Santo" está no INÍCIO da string? {}'.format(cidade[:5] == 'Santo'))  # no início da string
print('A palavra "Santo" está NA string? {}'.format('Santo' in cidade))  # em algum lugar na string
