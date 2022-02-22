from random import randint
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range (0,3):
        matriz [l] [c] = (randint(0,500))
print('A matriz randomizada foi: ')
for l in range(0,3):
    print() 
    for c in range (0,3):
        print (f'[{matriz [l] [c]:^5}]', end='    ')
        