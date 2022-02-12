from random import randint
x = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10))
print(f'Os números escolhidos foram: {x}.')
y = sorted(x)
print(f'O maior número foi {y[4]}')
print(f'O menor número foi {y[0]}')
