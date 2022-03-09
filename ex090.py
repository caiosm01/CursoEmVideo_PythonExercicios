aluno = {}
aluno['nome'] = str(input('Informe o nome do aluno:')).strip().title()
n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a segunda nota:'))
n3 = float(input('Informe a terceira nota:'))
aluno['média'] = (n1 + n2 + n3)/3
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'- {k} = {v}')
    print('-'*30)