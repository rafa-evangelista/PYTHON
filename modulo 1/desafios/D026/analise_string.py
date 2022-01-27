frase = str(input('Digite uma frase: ')).strip().capitalize()
print('A frase digitada foi: {}'.format(frase))
print('A letra "a" está presente {} vezes na frase.'.format(
    frase.lower().count('a')))
print('A letra "a" aparece na posição {} pela primeira vez.'.format(
    frase.lower().find('a')+1))
print('A letra "a" aparece na posição {} pela última vez.'.format(
    frase.lower().rfind('a')+1))
print('A variável possui {} letras (sem contar os espaços).'.format(
    len(frase)-frase.count(' ')))
