tupla = tuple(int(input(f'Informe o {i + 1}° valor:')) for i in range(0, 4))
pares = ()
print(f'Os valores digitados foram {tupla}.')
if tupla.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez.')
elif tupla.count(9) == 1:
    print('O número 9 apareceu uma vez.')
else:
    print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 foi digitado primeiro na posição {tupla.index(3) + 1}.')
else:
    print(f'O número 3 não foi digitado.')
pares = tuple(tupla[i] for i in range(0, 4) if tupla[i] % 2 == 0)
if len(pares) == 0:
    print('Não tem números pares entre os valores informados.')
elif len(pares) == 1:
    print(f'O número par é {pares}')
else:
    print(f'Os números pares são {pares}')
