'''from random import randint
tabela = tuple((randint(0, 10) for i in range(5)))
print(f'Os valores sorteados foram: {tabela}.\nO maior: {max(tabela)}\nO menor: {min(tabela)}')'''



'''from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior: {max(numeros)}\nO menor: {min(numeros)}')'''


from random import randint
numeros = tuple(int(input(f'Informe o {i+1}° número:')) for i in range (0, 5))
print(numeros)
print(f'\nO maior: {max(numeros)}\nO menor: {min(numeros)}')