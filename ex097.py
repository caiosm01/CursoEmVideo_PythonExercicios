def escreva(mensagem):
    print('~'*(len(mensagem) + 2))
    print(f' {mensagem}')
    print('~' * (len(mensagem) + 2))


msg = str(input('Escreva uma mensagem qualquer:'))
escreva(msg)
