lista = []
for c in range(0, 5):
    cont = 0
    num = int(input('Informe um número:'))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'O valor {num} foi adicionado no final da lista')
    else:
        while num in lista:
            num = int(input('Valor repetido, tente novamente. Digite um número:'))
        for i, v in enumerate(lista):
            if num > v:
                cont += 1
        lista.insert(cont, num)
        print(f'O valor {num} foi adicionado na posição {lista.index(lista[cont])}')
print(lista)