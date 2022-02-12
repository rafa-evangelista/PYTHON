while True:
    num = int(
        input('Quer ver a tabuada de qual valor (digite número negativo para sair):  '))
    if num < 0:
        break
    for i in range(0, 11):
        print(f'{num} x {i} = {num * i}')
    print('='*30)
