while True:
    print("""
    ==========================================
                CAIXA ELETRÔNICO
    ==========================================
    """)

    valor = int(input('Qual valor deseja sacar:  R$ '))
    print('')

    nota_50 = valor//50
    resto = valor % 50

    nota_20 = resto // 20
    resto = resto % 20

    nota_10 = resto // 10
    resto = resto % 10

    print(f'Total de {nota_50} cédulas de R$ 50,00')
    print(f'Total de {nota_20} cédulas de R$ 20,00')
    print(f'Total de {nota_10} cédulas de R$ 10,00')
    print(f'Total de {resto} cédulas de R$ 1,00')
    print('==========================================')
    print('Volte sempre ao Caixa Eletrônico! Tenha um bom dia!')

    saque = str(
        input('Deseja sacar mais algum valor [S] ou [N]:  ').strip() .upper())[0]
    if saque == 'N':
        break
