while True:
    num = int(input('Informe o número para ver sua tabuada:'))
    if num < 0:
        break
    print('=-='*14)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=-=' * 14)
print('=-='*14)
print('Programa encerrado. Volte sempre!')