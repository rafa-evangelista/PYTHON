import math
cat_oposto=float(input('Digite o comprimento do cateto oposto: '))
cat_adjacente=float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é {:.2f}.'.format(math.hypot(cat_oposto, cat_adjacente)))