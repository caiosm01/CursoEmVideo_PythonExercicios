from time import sleep


def valores(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(2.5)
    if len(num) == 0:
        print('Nenhum valor informado.')
    else:
        for n in num:
            sleep(0.5)
            print(n, end=' ')
        print(f'\nForam informados ao todo {len(num)} valores.')
        sleep(3)
        print(f'O maior valor informado foi: {max(num)}')
        sleep(3)


valores(2, 9, 4, 5, 7, 1)
valores(4, 7, 0)
valores(1, 2)
valores(6)
valores()
