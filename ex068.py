from random import randint
cont = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    computador = randint(0,100)
    n=int(input('Digite um valor:'))
    escolha = ' '
    while escolha not in 'PI':
        escolha=str(input('Par ou ímpar? [P/I]:')).strip().upper()[0]
    print('-'*20)
    total = computador + n
    print(f'Você jogou {n} e o computador {computador}. total de {total}.', end=' ')
    if escolha == 'P':
        if total % 2 == 0:
            print('DEU PAR.')
            print('-' * 20)
            print('você VENCEU!!')
            print('Vamos jogar novamente...')
            cont += 1
        elif total % 2 != 0:
            print('DEU ÍMPAR.')
            print('-' * 20)
            print('você PERDEU!!')
            break
    elif escolha == 'I':
        if total % 2 == 0:
            print('DEU PAR.')
            print('-' * 20)
            print('você PERDEU!!')
            break
        elif total % 2 != 0:
            print('DEU ÍMPAR.')
            print('-' * 20)
            print('você VENCEU!!')
            print('Vamos jogar novamente...')
            cont += 1
if cont == 1:
    print(f'GAME OVER! você me venceu {cont} vez.')
else:
    print(f'GAME OVER! você me venceu {cont} vezes.')