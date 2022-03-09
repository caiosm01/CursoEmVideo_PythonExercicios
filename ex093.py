dados = {} ; gols = list()
dados['Nome'] = str(input('Nome do jogador:')).strip().title()
njogos = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
for c in range(0, njogos):
    gols.append(int(input(f'Quantos gols na partida {c+1}?')))
dados['gols'] = gols[:]
dados['Total'] =sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'=> N° de gols na partida {i+1}: {v} ')
print(f'=> Total de gols: {dados["Total"]}')
