from datetime import date
maior=0
menor=0
for i in range(1,8):
    nome=str(input('Qual o nome da {}ª pessoa:  '.format(i))).strip().upper()
    ano_nasc=int(input('Qual o ano de nascimento de {}: '.format(nome)))
    ano_atual=date.today().year
    idade=int(ano_atual - ano_nasc)
    print('{} tem (ou completará) {} anos no ano de {}.'.format(nome, idade, ano_atual))
    if idade >=18:
        maior+=1
    else:
        menor+=1
print('Ao todo, {} pessoas atingiram a maioridade e {} pessoas ainda não atingiram.'.format(maior, menor))
