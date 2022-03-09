from time import sleep
escolha = 0; i=0; lista=[1]; soma = 0; multiplicar = 1; cont = 0
print('digite "-1" para parar')
while lista[i] != -1:
    lista.append(float(input('Informe o {}° número:'.format(i + 1))))
    soma += lista[i]
    multiplicar = multiplicar * lista[i]
    cont += 1
    i += 1
while escolha != 5:
    print('''opções...
    [1]- somar
    [2]- multiplicar
    [3]- maior
    [4]- novos números
    [5]- sair programa''')
    escolha=int(input('Sua escolha:'))
    if escolha == 1:
        print('A soma dos {} números informados é {}.'.format(cont-1, soma-1))
    elif escolha == 2:
        print('A multiplicação dos {} números informados é {}.'.format(cont-1, multiplicar))
    elif escolha == 3:
        print('O maior número entre os {} números informados é {}.'.format(cont-1, max(lista)))
    elif escolha == 4:
        print('Tente novamente.')
        print('=-=' * 10)
        sleep(2)
        i=0
        while lista[i] != -1:
            lista.append(float(input('Informe o {}° número:'.format(i + 1))))
            soma += lista[i]
            multiplicar = multiplicar * lista[i]
            cont += 1
            i += 1
    print('=-=' * 10)
    sleep(2)
print('Programa encerrado com sucesso')
print('=-='*10)
