def notas(lst, sit=False):
    """

    :param lst: lista com notas de vários alunos.
    :param sit: valor opcional, indicando se devo ou não adicionar a situação.
    :return: dicionário com várias informações sobre a turma.
    """
    dados = dict()
    dados['Quantidade de notas'] = len(lst)
    dados['A maior nota'] = max(lst)
    dados['A menor nota'] = min(lst)
    dados['A média da turma'] = sum(lst)/len(lst)
    if sit:
        if dados['A média da turma'] < 5:
            dados['Situação'] = 'RUIM'
        elif 5 <= dados['A média da turma'] < 7:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'BOA'
    return dados


nota = list()
i = 1
while True:
    nota.append(float(input(f'Digite a {i}° nota:')))
    resposta = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Tente novamente. Deseja continuar?[S/N]:')).strip().upper()[0]
    if resposta == 'N':
        break
    i += 1
op = str(input('Deseja mostrar a situação?[S/N]')).strip().upper()[0]
while op not in 'SN':
    op = str(input('Deseja mostrar a situação?[S/N]')).strip().upper()[0]
if op == 'S':
    print(notas(nota, sit=True))
help(notas)
