'''n1=float(input('Informe o primeiro número:'))
n2=float(input('Informe o segundo número:'))
n3=float(input('Informe o terceiro número:'))
if n1>n2 and n1>n3 and n2>n3:
    print('O maior é: {}\nO menor é:{}.'.format(n1, n3))
if n1>n2 and n1>n3 and n3>n2:
    print('O maior é: {}\nO menor é:{}.'.format(n1, n2))
if n2 > n1 and n2 > n3 and n3 > n1:
    print('O maior é: {}\nO menor é:{}.'.format(n2, n1))
if n2 > n1 and n2 > n3 and n1 > n3:
    print('O maior é: {}\nO menor é:{}.'.format(n2, n3))
if n3 > n1 and n3 > n2 and n1 > n2:
    print('O maior é: {}\nO menor é:{}.'.format(n3, n2))
if n3 > n1 and n3 > n2 and n2 > n1:
    print('O maior é: {}\nO menor é:{}.'.format(n3, n1))'''

a=int(input('Informe o primeiro valor:'))
b=int(input('informe o segundo valor: '))
c=int(input('informe o terceiro valor: '))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O maior valor é: {}.\nO menor valor é: {}.'.format(maior, menor))