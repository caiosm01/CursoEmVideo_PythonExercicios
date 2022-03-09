lista = []
cont = 1
while True:
    num = int(input(f'Informe o {cont}° número:'))
    lista.append(num)
    resposta = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    cont += 1
    if resposta == 'N':
        break
print('-='*30)
print(f'Foi digitado um número' if len(lista) == 1 else f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista na ordem decrescente: {lista}')
print(f'O valor "5" está na lista.' if 5 in lista else f'O valor "5" não está na lista.')
print('-='*30)