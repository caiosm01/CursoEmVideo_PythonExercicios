from random import randint
from time import sleep
from operator import itemgetter
jogador = {} ; ordem = list()
for c in range(0, 4):
    jogador[f'jogador {c+1}'] = randint(1, 6)
print('Valores sorteados:')
sleep(1)
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
ordem = sorted(jogador.items(), key= itemgetter(1), reverse= True)
print(f'{"==RANKING==":-^40}')
print(f'{"Posição":<10}{"Jogador":^20}{"Ponto":>10}')
print('-'*40)
for k, v in enumerate(ordem):
    print(f'{k+1:<10}{v[0]:^20}{v[1]:>10}')
    print('-'*40)
