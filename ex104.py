def leia(num):
    n1 = str(input(num))
    if n1.isnumeric():
        print(n1.isnumeric())
        return n1
    else:
        while not n1.isnumeric():
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            n1 = str(input(num))
        return n1


n = leia('Digite um número inteiro:')
print(f'Você acabou de digitar o número {n}.')
