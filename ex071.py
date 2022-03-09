print('='*40)
print(f'{"BANCO CAIO":^40}')
print('='*40)
valor=int(input('Informe o valor que deseja sacar: R$'))
print('='*40)
ced50 = valor // 50
valor %= 50
ced20 = valor // 20
valor %= 20
ced10 = valor // 10
valor %= 10
ced1 = valor // 1
valor %= 1
print('O saque terá:')
if ced50 > 0:
    print(f'{ced50} notas de cinquenta reais')
if ced20 > 0:
    print(f'{ced20} notas de vinte reais')
if ced10 > 0:
    print(f'{ced10} notas de dez reais')
if ced1 > 0:
    print(f'{ced1} notas de um reais')
print('='*40)





'''print('='*40)
print(f'{"BANCO CAIO":^40}')
print('='*40)
valor=int(input('Informe o valor que deseja sacar: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced != 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*40)
print('VOLTE SEMPRE AO BANCO CAIO!')'''


'''valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")'''

