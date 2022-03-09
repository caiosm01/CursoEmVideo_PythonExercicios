c = 1
num=int(input('Informe o {}° número:'.format(c)))
soma = num
maior = menor = num
resposta=str(input('Deseja continuar?')).strip().upper()[0]
while resposta == 'S':
    c += 1
    num = int(input('Informe o {}° número:'.format(c)))
    soma += num
    resposta = str(input('Deseja continuar?')).strip().upper()[0]
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
media = soma/c
if resposta not in 'SN':
    print('Opção inválida. Tente novamente.')
elif resposta in 'SN':
    print('Foram informados {} valores e a média entre eles é {}.'.format(c, media))
    print('O maior valor informado foi o {} e o menor foi o {}.'.format(maior, menor))
