def area(a,c):
    t = a * c
    return t

#Bloco Principal
print('CONTROLE DE TERRENOS')
print('='*22)

larg = float(input('Qual a largura do terreno [m]:  '))
alt = float (input('Qual a comprimento do terreno [m]: '))

total = area (larg, alt)

print(f'As medidas do terreno são {larg} m x {alt} m e a área total é de {total} m2.')
