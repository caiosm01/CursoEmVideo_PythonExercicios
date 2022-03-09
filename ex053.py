'''frase = str(input('Informe uma frase para verificar se é um palíndromo:')).upper().strip().split()
frase1=''.join(frase)
print('A frase {} ao contrário fica, {}.'.format(frase1, frase1[len(frase1)::-1]))
if frase1 == frase1[len(frase1)::-1]:
    print('Por isso é um palíndromo')
else:
    print('Por isso não é um palíndromo.')'''



frase = str(input('Informe uma frase para verificar se é um palíndromo:')).upper().strip().split()
frase1=''.join(frase)
cont=0
soma=''
for c in range(len(frase1)-1,-1,-1):
    soma+=frase1[c]
    if frase1[cont]==frase1[c]:
        cont+=1
print('A frase {} ao contrário fica, {}.'.format(frase1, frase1[len(frase1)::-1]))
if cont == len(frase1):
    print('Por isso é um palíndromo')
else:
    print('Por isso não é um palíndromo.')