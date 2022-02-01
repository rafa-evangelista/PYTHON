lado1 = float(input('Digite o comprimento da reta 1: '))
lado2 = float(input('Digite o comprimento da reta 2: '))
lado3 = float(input('Digite o comprimento da reta 3: '))
if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado3 + lado2) > lado1):
    print('As retas {}, {} e {} formam um triângulo.'.format(lado1, lado2, lado3))
else:
    print('As retas {}, {} e {} nao podem formar um triângulo.'.format(
        lado1, lado2, lado3))
