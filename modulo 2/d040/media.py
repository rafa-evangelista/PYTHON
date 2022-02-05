nota1 = float(input('Digite a primeira nota:  '))
nota2 = float(input('Digite a segunda nota:  '))
media = ((nota1 + nota2) / 2)
if media < 5.0:
    print('Aluno com média {}.  REPROVADO.'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Aluno com média {}. RECUPERAÇÃO.'.format(media))
else:
    print('Aluno com média {}. APROVADO.'.format(media))
