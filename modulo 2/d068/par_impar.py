from random import randint

print('.'*35)
print('PAR OU ÍMPAR')
print('.'*35)

soma = 0
while True:

    comp = randint(1, 10)
    minha_escolha = str(
        input('Você escolhe PAR ou ÍMPAR [P] ou [I]?  ')).strip().upper()[0]
    if minha_escolha == 'P':
        escolha_computador = 'I'
    else:
        escolha_computador = 'P'

    eu = int(input('Escolha um número:  '))

    resultado = (eu + comp)
    if resultado % 2 == 0:
        res_final = 'PAR'
    else:
        res_final = 'IMPAR'

    if res_final[0] == minha_escolha:
        soma += 1
        print(
            f'O computador escolheu {comp} e você escolheu {eu}. Deu {res_final}. VOCÊ GANHOU!!!')
    else:
        print(
            f'O computador escolheu {comp} e você escolheu {eu}. Deu {res_final}. VOCÊ PERDEU!!!')
        break

print(f'Você ganhou {soma} vezes consecutivas!!!')
