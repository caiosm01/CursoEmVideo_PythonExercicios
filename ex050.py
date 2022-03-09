acumulador=0
cont=0
for c in range(1,7):
    n=int(input('Informe um número inteiro:'))
    if n % 2 == 0:
        acumulador=acumulador+n
        cont=cont+1
print('A soma dos {} números pares informados é {}.'.format(cont, acumulador))