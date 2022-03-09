dados = {} ; pessoas = [] ; mulher = [] ; acimadamedia = []
i = 1
soma = 0
while True:
    dados['Nome'] = str(input(f'Nome da {i}° pessoa:')).strip().title()
    dados['Sexo'] = str(input(f'Sexo da {i}° pessoa [M/F]:')).strip().upper()[0]
    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input(f'ERRO: Por favor, digite apenas "M" ou "F".\nSexo da {i}° pessoa [M/F]:')).strip().upper()[0]
    if dados['Sexo'] == 'F':
        mulher.append(dados['Nome'])
    dados['Idade'] = int(input(f'Idade da {i}° pessoa:'))
    soma += dados['Idade']
    pessoas.append(dados.copy())
    resposta = str(input('Deseja continuar?[N/S]:')).strip().upper()[0]
    while resposta not in 'NS':
        resposta = str(input('ERRO: Por favor, digite apenas "N" ou "S".\nDeseja continuar?[N/S]:')).strip().upper()[0]
    if resposta == 'N':
        break
    i += 1
print('-='*30)
print(f'A) Número de pessoas cadrastradas: {len(pessoas)}')
print(f'B) Média de idade: {soma/i}')
print(f'C) Mulheres cadastradas: {mulher}')
print('D) Lista de pessoas com idade acima da média:')
for p in pessoas:
    if p['Idade'] > soma/i:
        acimadamedia.append(p.copy())
for n in acimadamedia:
    for k, v in n.items():
        print(f'{k} = {v}; ', end='')
    print()
