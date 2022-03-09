def aumentar(n = 0, taxa = 0):
    total = n + (n * taxa/100)
    return total


def diminuir(n = 0, taxa = 0):
    total = n - (n * taxa/100)
    return total


def dobro(n = 0):
    return n * 2


def metade(n = 0):
    return n/2


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
