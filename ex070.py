total = maisdemil = i = cont = barato = caro = 0
nomemaisdemil = []
nomemaiscaro = nomemaisbarato = ' '
print('=-='*21)
print('{:^60}'.format('LOJAS SUPER BARATÃO'))
print('=-='*21)
while True:
    escolha = ' '
    nome = str(input(f'nome do {cont + 1}° produto:')).strip().title()
    valor = float(input('Preço: R$'))
    cont += 1
    total += valor
    if valor > 1000:
        maisdemil += 1
        nomemaisdemil.insert(i, nome)
        i += 1
    if cont == 1:
        barato = caro = valor
        nomemaiscaro = nomemaisbarato = nome
    else:
        if barato > valor:
            barato = valor
            nomemaisbarato = nome
        if caro < valor:
            caro = valor
            nomemaiscaro = nome
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if escolha == 'N':
        break
    print('=-=' * 21)
print(f'{"FIM DO PROGRAMA":-^60}')
print(f'O total da compra foi de R${total:.2f}.')
if maisdemil == 1:
    print(f'\nTemos {maisdemil} produto custando mais de R$1000.00.\nSão eles: ', end='')
    for a in range (0, i):
        print(f'{nomemaisdemil[a]}', '.' if nomemaisdemil[a] == nomemaisdemil[i-1] else ',', end='')
elif maisdemil > 1:
    print(f'\nTemos {maisdemil} produtos custando mais de R$1000.00.\nSão eles: ', end='')
    for a in range(0, i):
        print(f'{nomemaisdemil[a]}', '.' if nomemaisdemil[a] == nomemaisdemil[i - 1] else ',', end='')
print(f'\nO produto mais barato foi {nomemaisbarato} que custou R${barato:.2f}')
print(f'\nO produto mais caro foi {nomemaiscaro} que custou R${caro:.2f}')