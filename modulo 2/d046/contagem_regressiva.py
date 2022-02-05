from time import sleep
import os

for cont in range (10, 0, -1):
    print("""
----------------------------------------------------------
                  CONTAGEM REGRESSIVA
----------------------------------------------------------

Contagem regressiva para o estouro dos fogos de artifício
""")

    print('Faltam {} segundos.'.format(cont))
    sleep(1)
    os.system('cls')    

print("""
----------------------------------------------------------
                  CONTAGEM REGRESSIVA
----------------------------------------------------------

Feliz Ano Novo!

""")
 
