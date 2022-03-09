def ficha(jog = '<desconhecido>', gol = 0):
    return f'O jogador {jog} fez {gol} gol(s) no campeonato.'


n = str(input('Nome do jogador:')).strip().title()
g = str(input('Número do gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    print(ficha(gol=g))
else:
    print(ficha(n,g))


'''def ficha(n='<desconhecido>', g='0'):
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


nome = str(input('Informe o nome do jogador:'))
gols = str(input('Número de gols:'))
if nome == '':
    if gols == '' or gols not in '1234567890':
        print(ficha())
    elif gols in '1234567890':
        print(ficha(g=gols))
if nome != '':
    if gols == '' or gols not in '1234567890':
        print(ficha(n=nome))
    elif gols in '1234567890':
        print(ficha(n=nome, g=gols))'''
