c = ('\033[m',         #0-sem cor
     '\033[0;30;41m',  #1-vermelho
     '\033[0;30;42m',  #2-verde
     '\033[0;30;43m',  #3-amarelo
     '\033[0;30;44m',  #4-azul
     '\033[0;30;45m',  #5-roxo
     '\033[7;30m')     #6-branco


def ajuda(opcao):
    from time import sleep
    titulo(f'Acessando o manual do comando "{opcao}"', 3)
    sleep(1)
    print(c[6], end='')
    help(opcao)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    op = str(input('\033[mFunção ou Biblioteca > '))
    if op == 'fim':
        titulo('ATÉ LOGO', 4)
        break
    ajuda(op)
