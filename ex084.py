dados = list() ; pessoas = list() ; pesadas = list() ; leves = list ()
c = maior = menor = 0
while True:
    dados.append(str(input(f'Informe o nome da {c + 1}° pessoa:')).strip().title())
    dados.append(float(input(f'Informe o peso da {c + 1}° pessoa:')))
    if len(pessoas) == 0:
       maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    c += 1
    resposta = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
print('=-='*20)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('=-='*20)
for p in pessoas:
    if p[1] == maior:
        pesadas.append(p[0])
    elif p[1]== menor:
        leves.append(p[0])
print(f'Maior peso: {maior}kg.\npessoas com esse peso: {pesadas}')
print('=-='*20)
print(f'Menor peso: {menor}kg.\npessoas com esse peso: {leves}')
