lista = []
while True:
    num = int(input('Digite um número:'))
    while num in lista:
        num = int(input('Valor repetido, tente novamente. Digite um número:'))
    lista.append(num)
    resposta = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
    elif resposta not in 'NS':
        resposta = str(input('Tente novamente. Deseja continuar?[S/N]:')).strip().upper()[0]
print('-='*30)
lista.sort()
print(f'Os valores digitados, em ordem crescente foram: {lista}')
