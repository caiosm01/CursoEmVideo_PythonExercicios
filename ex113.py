def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida.')
            return 0
        else:
            return n1


num1 = leiaInt('Digite um número inteiro: ')
num2 =leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {num1} e o número real {num2}.')
