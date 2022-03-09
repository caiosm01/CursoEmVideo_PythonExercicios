eq = str(input('Digite uma expressão:'))
lista = []
for c in eq:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')




'''eq = str(input('Informe uma equação matemática:'))
if eq.count('(') == eq.count(')'):
    print('Equação válida.')
else:
    print('Equação inválida.')'''
