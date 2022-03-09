from math import ceil
dados = list() ; alunos = list()
while True:
    dados.append(str(input('Nome:')).strip().title())
    dados.append(float(input('Nota 1:')))
    dados.append(float(input('Nota 2:')))
    dados.append((dados[1]+dados[2])/2)
    alunos.append(dados[:])
    dados.clear()
    resposta = str(input('Deseja continuar?')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Tente novamente. Deseja continuar?')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*20)
print(f'{"N°":<10}', f'{"NOME":<10}', f'{"MÉDIA":>10}')
print('--'*20)
for i, c in enumerate(alunos):
    print(f'{i:<10}', f'{c[0]:<10}', f'{c[3]:>10.2f}')
    print('--'*20)
while True:
    escolha = str(input('Deseja ver os dados de algum aluno?[S/N]:')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input('Tente novamente. Deseja ver os dados de algum aluno?[S/N]:')).strip().upper()[0]
    if escolha == 'N':
        break
    novo = int(input('Qual?[N°]:'))
    print(f'Nome: {alunos[novo][0]}\nNota 1: {alunos[novo][1]}\nNota 2: {alunos[novo][2]}')
