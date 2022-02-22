import datetime

dados = {}

print(f'*'*70)
print('                        CADASTRO DE FUNCIONÁRIOS')
print(f'*'*70)
dados['nome'] = str(input('Digite o nome do funcionário: ')).strip().upper()
dados['nascimento'] = int(
    input(f'Digite o ano de nascimento de {dados["nome"]}: '))
dados['idade'] = datetime.date.today().year - dados['nascimento']
dados['ctps'] = int(
    input(f'Digite CTPS do funcionário {dados["nome"]} [0 para não tem]: '))

if dados['ctps'] != 0:
    dados['ano_contratacao'] = int(
        input(f'Digite o ano de contratacao de {dados["nome"]}: '))
    dados['salario'] = float(
        input(f'Digite o salário de {dados["nome"]}: R$ '))
    dados['aposentadoria'] = (
        dados['ano_contratacao'] + dados['idade'] + 35) - datetime.date.today().year

print('='*70)
for k, v in dados.items():
    print(f'- {k} tem o valor de {v}.')
