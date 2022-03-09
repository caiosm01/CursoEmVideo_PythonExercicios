'''nome=str(input('Informe um nome completo:')).strip().title()
maiusculo=nome.upper()
dividido=maiusculo.split()
print('O nome {} possui "SILVA"? {}.'.format(nome, 'SILVA' in dividido))'''

'''nome1= str(input('Informe seu nome completo: ')).strip()
nome= nome1.title()
print('O nome {} possui Silva?'.format(nome))
if nome.find('Silva') == -1:
    print('false.')
else:
    print('true.')'''

nome=str(input('Informe um nome completo:')).strip().title()
print('O nome {} possui "Silva"?\n {}.'.format(nome, 'Silva' in nome))








