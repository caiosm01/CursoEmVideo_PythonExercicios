from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores...')
    sleep(1)
    for c in range(0, 5):
        sort = randint(0, 10)
        lista.append(sort)
        print(sort, end=' -> ')
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    print(f'Somando os valores pares de {lista}...')
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(soma)


numeros = []
sorteia(numeros)
somaPar(numeros)
