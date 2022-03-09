n1= int(input('Informe um número inteiro:'))
n2=int(input('Informe outro número inteiro:'))
if n1 > n2:
    print('o número {} é maior do que o número {}.'.format(n1, n2))
elif n1 < n2:
    print('o número {} é maior do que o número {}.'.format(n2, n1))
else:
    print('Não existe número maior. Os dois são iguais.')
