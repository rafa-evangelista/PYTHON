from time import sleep

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim}, passo {passo}: ')
    if passo == 0:
        passo += +1

    if inicio < fim:
        for i in range(inicio, (fim+1), passo):
            print(f'[{i}]   ', end='', flush=True)
            sleep(0.5)
        print('  >>> FIM')

    elif inicio > fim:
        if passo > 0:
            passo *= -1
            for i in range(inicio, (fim-1), passo):
                print(f'[{i}]   ', end='', flush=True)
                sleep(0.5)
            print('  >>> FIM')
        else:
            for i in range(inicio, (fim-1), passo):
                print(f'[{i}] ', end='', flush=True)
                sleep(0.5)
            print('  >>> FIM')
    else:
        print(inicio)


# Inicio do Programa
print('=' * 100)
print('CONTADOR')
print('=' * 100)

contador (1, 10, 1)
contador (10, 0, 2)

a = int(input('Agora é sua vez. Digite um número para o início da sequencia:  '))
b = int(input('Digite um número de fim da sequencia:  '))
c = int(input('Digite um "passo":  '))

contador(a, b, c)

print('=' * 100)
print('FIM DO PROGRAMA')
