def fatorial(n, show=False):
    """
    -> Função que calcula o fatorial de um número n.
    :param n: número que iremos calcular o fatorial.
    :param show: indica se irá ou não exibir o calculo na tela.
    :return: retorna o fatorial de n.
    """
    total = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        total *= c
    return total


num = int(input('Informe um número: '))
opcao = str(input('Deseja mostrar o cálculo? [S/N]:')).strip().upper()[0]
if opcao == 'S':
    print(fatorial(num, show=True))
elif opcao == 'N':
    print(fatorial(num, show=False))
