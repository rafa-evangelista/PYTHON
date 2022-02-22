import random 
aluno = ('Rafael', 'Mariana', 'Marcos', 'Júlia')
def selectrandom(aluno):
    return random.choice(aluno)
print ('O aluno escolhido para apagar o quadro foi ', random.choice(aluno))
