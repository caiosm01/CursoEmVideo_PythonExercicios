def leiaTexto(msg):
    while True:
        try:
            nome = str(input(msg)).strip().title()
            novo1 = nome.split()
            novo2 = ''.join(novo1)
            while not novo2.isalpha():
                print('ERRO! Digite um nome válido.')
                nome = str(input(msg)).strip().title()
                novo1 = nome.split()
                novo2 = '-'.join(novo1)
        except:
            print('ERRO!.')
            continue
        else:
            return nome
