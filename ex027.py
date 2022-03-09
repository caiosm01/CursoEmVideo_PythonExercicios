'''nome=str(input('Digite seu nome completo:')).strip().title()
dividido=nome.split()
a=nome.rfind(' ')
print('Seja bem vindo, {}!'.format(nome))
#print('Seu primeiro nome é {} e seu último nome é {}.'.format(dividido[0], nome[a+1:]))
print('Seu primeiro nome é {} e seu último nome é {}.'.format(dividido[0],dividido[len(dividido)-1]))'''

nome= str(input('Informe seu nome completo: ')).strip().title()
dividido=nome.split()
print('Prazer em te conhecer, {}!'.format(nome))
print('Seu primeiro nome é: {}.\nSeu ultimo nome é: {}.'.format(dividido[0], nome[nome.rfind(' ')+1:]))