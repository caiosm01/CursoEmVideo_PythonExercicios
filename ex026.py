'''frase=str(input('Digite uma frase qualquer:')).strip().upper()
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
print('A letra "A" aparece a primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece a ultima vez na posição {}.'.format(frase.rfind('A')+1))'''

frase= str(input('Informe uma frase: ')).strip().upper()
print('Essa frase possui {} letras "A".'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}.'.format(frase.rfind('A')+1))

