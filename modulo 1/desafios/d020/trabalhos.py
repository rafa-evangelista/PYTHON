import random
lista = ('Rafael', 'Mariana', 'Paulo', 'Júlia')


def selectrandom(lista):
    return random.choice(lista)


print('A ordem da apresentação dos trabalhos pelos alunos será: {}, {}, {} e {}'.format(
    random.choice(lista), random.choice(lista), random.choice(lista), random.choice(lista)))
