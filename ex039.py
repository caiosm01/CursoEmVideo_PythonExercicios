from datetime import date
print('''Escolha a o sexo
masculíno: 1
feminino: 2''')
sexo=int(input('Sua opção:'))
if sexo==1:
    nascimento=int(input('Informe o ano de seu nascimento:'))
    atual=date.today().year
    idade=atual-nascimento
    print('Quem nasceu no ano de {}, em {} tem {} anos.'.format(nascimento, atual, idade))
    if idade < 18:
        alistar=18-idade
        print('Você deverá se alistar daqui a {} anos, em {}.'.format(alistar, atual+alistar))
    elif idade > 18:
        alistar=idade-18
        print('Você deveria ter se alistado a {} anos atrás, em {}.'.format(alistar, atual-alistar))
    else:
        print('Você deve se alistar IMEDIATAMENTE.')
else:
    print('Você não é obrigada a se alistar.')