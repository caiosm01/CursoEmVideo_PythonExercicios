from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= (-1)
    elif p == 0:
        p = 1
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(2.5)
    if i > f:
        cont = i
        while cont >= f:
            print(cont, end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('INÍCIO:'))
fim = int(input('FIM:'))
passo = int(input('PASSO:'))
contador(inicio, fim, passo)
