numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Informe um número entre 0 e 20:'))
    if n > 20:
        print('Tente novamente.', end='')
    else:
        print(f'O número informado foi o {numeros[n]}.')
        resposta = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
        if resposta == 'N':
            break