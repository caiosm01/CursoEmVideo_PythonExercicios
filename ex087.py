matriz = list()
somapar = scoluna = 0
nl = int(input('Informe o número de linhas da matriz:'))
nc = int(input('Informe o número de colunas da matriz:'))
for l in range(0, nl):
    matriz.append([])
    for c in range(0, nc):
        num = int(input(f'Informe o valor para [{l},{c}]:'))
        matriz[l].append(num)
        if num % 2 == 0:
            somapar += num
        if c == 2:
            scoluna += num
print('=-='*30)
for l in range(0, nl):
    for c in range(0, nc):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
print('=-='*30)
print(f'Soma dos valores pares da matriz: {somapar}')
print(f'Soma dos valores da terceira coluna: {scoluna}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')