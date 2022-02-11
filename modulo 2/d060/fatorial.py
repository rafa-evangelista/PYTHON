n = int(input('Digite um número: '))
print(f'O fatorial do número {n} é ', end='')
fat = n
i = 1
while i != n:
    fat *= i
    i += 1
print(fat)
