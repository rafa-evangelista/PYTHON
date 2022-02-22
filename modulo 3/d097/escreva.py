def escreva(msg):
    a = (len(msg) + 12)
    print('=' * a)
    print(f'      {msg}')
    print('=' * a)


titulo = str(input('Digite o Título a ser exibido:  ')).strip().upper()
escreva(titulo)
