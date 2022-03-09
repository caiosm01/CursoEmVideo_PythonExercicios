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
