dist=float(input('Quantos Km foram percorridos: '))
dias=int(input('Quantos dias o carro ficou alugado: '))
preco_dia = dias * 60
preco_km = dist * 0.15
print('O carro ficou {} dias alugado e percorreu {}km.  O preço a pagar é de R$ {:.2f}.'.format(dias, dist, (preco_dia + preco_km)))
