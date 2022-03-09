lista = []
par = []
impar = []
cont = 1
while True:
    num = int(input(f'Informe o {cont}° número:'))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resposta = str(input('Quer continuar?[S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
    cont += 1
print('-='*30)
print(f'Lista completa: {lista}')
print(f'pares: {par}')
print(f'ímpares: {impar}')
print('-='*30)
