def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida.')
            return 0
        else:
            return n
