'''num=int(input('Informe o número de pessoas para analisar o maior e o menor peso:'))
peso=[]
i=0
for c in range(1, num+1):
    peso.insert(i, float(input('Informe o peso da {}° pessoa:'.format(c))))
    i+=1
print('O maior peso lido foi {} kg.\nO menor peso lido foi {} kg.'.format(max(peso), min(peso)))'''


num=int(input('Informe o número de pessoas para analisar o maior e o menor peso:'))
maior=0
menor=0
for c in range(1, num+1):
    peso=float(input('Informe o peso da {}° pessoa:'.format(c)))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior=peso
        if peso < menor:
            menor=peso
print('O maior peso informado foi {} kg.\nO menor peso informado foi {} kg.'.format(maior, menor))