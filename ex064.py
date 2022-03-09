cont = soma = 0
c = 1
num = int(input('Informe o {}° número(digite "-1" para parar):'.format(c)))
while num != -1:
    cont += 1
    c += 1
    soma += num
    num = int(input('Informe o {}° número(digite "-1" para parar):'.format(c)))
print('A soma dos {} números digitados foi {}.'.format(cont, soma))