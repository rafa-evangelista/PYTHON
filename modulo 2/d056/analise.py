print("""
-----------------------------------------------------------------
                      PROGRAMA DE ANÁLISES
-----------------------------------------------------------------""")
somaidade = 0
idademaior = 0
mmenos = 0
hvelho = ""
a = 0
for i in range(1, 6):
    print("""
    ----------------------------------------------------------
                         CANDIDATO """, i, """ 
    ----------------------------------------------------------""")
    nome = str(input('Qual o nome da {}ª pessoa: '.format(i))).strip().upper()
    idade = int(input('Qual a idade de {}: '.format(nome)))
    sexo = int(
        input('Qual o gênero de {} ([1] FEMININO; [2] MASCULINO): '.format(nome)))
    somaidade += +idade
    if sexo == 2 and idade > idademaior:
        idademaior = idade
        hvelho = nome
    if sexo == 1 and idade < 20:
        a += +1
print('')
media = somaidade/5
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O nome do homem mais velho é {} e sua idade é {}.'.format(hvelho, idademaior))
print('O grupo possui {} mulheres com menos de 20 anos.'.format(a))
print('')
