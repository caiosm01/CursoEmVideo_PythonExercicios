def area(a, b):
    mult = a * b
    print(f'A área de um terreno {a} x {b} é de {mult} m²...')


print(f'{"CONTROLE DE TERRENOS":^30}')
print('-'*30)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m):'))
area(l, c)
