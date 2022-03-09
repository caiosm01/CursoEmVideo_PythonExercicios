from ex115.ferramentas.titulo import cabecalho
from  ex115.ferramentas.validanumero import leiaInt
from ex115.ferramentas.linha import borda


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    borda()
    opc = leiaInt('Opção: ')
    while opc > len(lista) or opc < 1:
        print('ERRO! digite uma das opções acima.')
        opc = leiaInt('Opção: ')
    return opc
