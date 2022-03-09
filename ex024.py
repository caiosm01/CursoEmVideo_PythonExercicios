'''nome=str(input('Informe a cidade em que você nasceu:')).strip()
cidade=nome.title()
dividido=cidade.split()
print('A cidade {} começa com o nome "Santo":'.format(cidade))
print('Santo'==dividido[0])
print(cidade[1:10:2])'''

nome1= str(input('Informe a cidade em que você nasceu: ')).strip()
nome= nome1.title()
cidade= nome.split()
print('A cidade {} começa com o nome "Santo":'.format(nome))
if cidade[0] == 'Santo':
    print('true.')
else:
    print('false')