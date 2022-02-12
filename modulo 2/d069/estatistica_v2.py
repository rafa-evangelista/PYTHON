maioridade = homens = mulheres = 0

while True:
    print("""
    -----------------------------------------------------------------
                       CADASTRO DE PESSOAS
    -----------------------------------------------------------------
    """)

    idade = int(input('Qual a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M] ou [F]:  ')).strip().upper()[0]

    if idade > 18:
        maioridade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(
            input('Deseja continuar [S] ou [N]:  ')).strip() .upper()[0]
    if continuar == 'N':
        break

print('-'*50)
print(f'Ao todo {maioridade} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados no sistema.')
print(f'{mulheres} mulheres com menos de 20 anos estão cadastradas.')
