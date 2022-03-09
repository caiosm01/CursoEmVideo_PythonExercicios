maioridade = homem = mulher = i = j = k = 0
nomehomem = []
nomemulher = []
nomemaioridade = []
while True:
    escolha = ' '
    sexo = ' '
    print('-=' * 20)
    print('CADASTRE UMA PESSOA!')
    print('-='*20)
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]:')).strip().upper()[0]
    print('-=' * 20)
    if idade > 18:
        maioridade += 1
        nomemaioridade.insert(i, nome)
        i += 1
    if sexo == 'M':
        homem += 1
        nomehomem.insert(j, nome)
        j += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
        nomemulher.insert(k, nome)
        k += 1
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}\nNomes: ', end='')
for c in range(0, i):
    print(f'{nomemaioridade[c]}','.' if nomemaioridade[c] == nomemaioridade[i-1] else ', ', end='')
if homem == 1:
    print('\nAo todo temos 1 homem cadastrado.\nNome: ', end='')
    for c in range(0, j):
        print(f'{nomehomem[c]}.')
else:
    print(f'\nAo todo temos {homem} homens cadastrados.\nNomes: ', end='')
    for c in range(0, j):
        print(f'{nomehomem[c]}','.' if nomehomem[c] == nomehomem[j-1] else ', ',  end='')
if mulher == 1:
    print('\nE temos 1 mulher com menos de 20 anos.\nNome: ', end='')
    for c in range(0, k):
        print(f'{nomemulher[c]}.')
else:
    print(f'\nE temos {mulher} mulheres com menos de 20 anos.\nNomes: ', end='')
    for c in range(0, k):
        print(f'{nomemulher[c]}','.' if nomemulher[c] == nomemulher[k-1] else ', ', end='')