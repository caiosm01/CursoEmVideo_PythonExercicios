def aumentar(n=0, taxa=0, formata=False):
    total = n + (n * taxa/100)
    return total if formata is False else moeda(total)


def diminuir(n=0, taxa=0, formata=False):
    total = n - (n * taxa/100)
    return total if formata is False else moeda(total)


def dobro(n=0, formata=False):
    return n*2 if formata is False else moeda(n*2)


def metade(n=0, formata=False):
    return n/2 if formata is False else moeda(n/2)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(n=0, aumento=10, diminui=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n, aumento, True)}')
    print(f'{diminui}% de redução: \t\t{diminuir(n, diminui, True)}')
    print('-' * 30)
