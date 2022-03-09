matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Informe o valor para [{l},{c}]:'))
        matriz[l].append(num)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()