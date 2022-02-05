r1 = int(input('Digite o comprimento da reta 1: '))
r2 = int(input('Digite o comprimento da reta 2: '))
r3 = int(input('Digite o comprimento da reta 3: '))
if ((r1+r2)>=r3) and ((r1+r3)>=r2) and ((r3+r2)>=r1):
    if r1 == r2 and r1 == r3:
        print("As retas formam um triangulo equilátero")
    elif r1!=r3 and r1!=r2 and r2!=r3:
        print('As retas formam um triangulo escaleno')
    else:
        print('As retas formam um triangulo isósceles')
else:
    print('As retas NÃO formam um triangulo')
