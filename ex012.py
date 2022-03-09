p=float(input('Informe o preço do produto: R$'))
des=p-(p*0.05)
print('O produto que custava R${:.2f}, com um desconto de 5%, passa a valer R${:.2f}.'.format(p, des))
