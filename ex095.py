dados = {} ; gols = list(); jogadores = []
while True:
    dados['Nome'] = str(input('Nome do jogador:')).strip().title()
    njogos = int(input(f'Quantas partidas {dados["Nome"]} jogou?'))
    for c in range(0, njogos):
        gols.append(int(input(f'Quantos gols na partida {c+1}?')))
    dados['gols'] = gols[:]
    dados['Total'] =sum(gols)
    gols.clear()
    jogadores.append(dados.copy())
    resposta = str(input('Deseja continuar?[N/S]:')).strip().upper()[0]
    while resposta not in 'NS':
        resposta = str(input('ERRO: Por favor, digite apenas "N" ou "S".\nDeseja continuar?[N/S]:')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*30)
print(f'{"cod":<15}{"nome":<15}{"gols":<15}{"total":<15}')
print('--'*30)
for p in range(0, len(jogadores)):
    print('{:<15}{:<15}{:<15}{:<15}'.format(p, jogadores[p]['Nome'], str(jogadores[p]['gols']), jogadores[p]['Total']))
    print('--'*30)
while True:
    escolha = int(input('Mostrar dados de qual jogador?(999 parar):'))
    if escolha == 999:
        print('==>VOLTE SEMPRE!<==')
        break
    elif escolha not in range(0, len(jogadores)):
        print('ERRO. Digite um dos códigos da tabela.')
    elif escolha in range(0, len(jogadores)):
        print(f'O jogador {jogadores[escolha]["Nome"]} jogou {len(jogadores[escolha]["gols"])} partidas.')
        for i, v in enumerate(jogadores[escolha]['gols']):
            print(f'=> N° de gols na partida {i + 1}: {v} ')
        print(f'=> Total de gols: {jogadores[escolha]["Total"]}')
        print('-'*40)
