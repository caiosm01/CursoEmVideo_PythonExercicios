from random import randint
from time import sleep
jogos = list()
print('=='*30)
print(f'{"JOGO DA MEGA SENA":-^60}')
print('=='*30)
njogos = int(input('Quantos jogos você quer? '))
for n in range(0, njogos):
    jogos.append([])
    for num in range(0, 6):
        sort = randint(1, 60)
        if num == 0:
            jogos[n].append(sort)
        elif num > 0:
            while sort in jogos[n]:
                sort = randint(1, 60)
#            for c in range(0, num):
#                if sort == jogos[n][c]:
#                    while sort == jogos[n][c]:
#                        sort = randint(1, 60)
            jogos[n].append(sort)
    sleep(1)
    print(f'Jogo {n+1}: {jogos[n]}')

