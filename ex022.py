'''nome=str(input('Informe seu nome completo:')).strip()
print('Seu nome com todas as letras maiúsculas fica dessa forma: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica dessa forma: {}.'.format(nome.lower()))
print('Seu nome completo possui {} letras.'.format(len(nome)-nome.count(' ')))
dividido=nome.split()
print('O primeiro nome tem {} letras.'.format(len(dividido[0])))
#print('O primeiro nome tem {} letras.'.format(nome.find(' ')))'''

n1= str(input('Informe seu nome completo:'))
nome=n1.strip()
print('Seu nome com todas as letras maiúsculas fica assim: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica assim: {}'.format(nome.lower()))
espaço=nome.count(' ')
letras=len(nome)-espaço
print('Seu nome possui {} letras.'.format(letras))
dividido= nome.split()
primeiro=len(dividido[0])
print('Seu primeiro nome tem {} letras.'.format(primeiro))