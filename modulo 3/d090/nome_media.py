dados = {}

dados['nome'] = str(input('Qual o nome do aluno: ')).strip().upper()
nota1 = float(input(f'Digite a primeira nota de {dados["nome"]}: '))
nota2 = float(input('Digite a segunda nota: '))
media = float((nota1 + nota2)/2)
dados['media'] = media
if media < 5.0:
    dados['situacao'] = 'Reprovado'
elif media < 7.0:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Aprovado'

print(
    f'O aluno {dados["nome"]} tem média de {dados["media"]:.2f} e a situação é {dados["situacao"]}.')
