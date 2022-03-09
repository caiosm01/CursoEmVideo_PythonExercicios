numero=int(input('Informe um número inteiro qualquer:'))
print('binário: 1')
print('octal: 2')
print('hexadecimal: 3')
base=int(input('escolha a base de conversão desejada:'))
if base == 1:
    print('O número {} convertido para a base binária é {}.'.format(numero, bin(numero)[2:]))
elif base ==2:
    print('O número {} convertido para a base octal é {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O número {} convertido para a base binária é {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')