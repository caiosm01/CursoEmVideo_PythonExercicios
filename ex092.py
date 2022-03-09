from datetime import date
registro = {}
registro['nome'] = str(input(f'Informe o nome da pessoa:')).strip().title()
nascimento = int(input(f'Informe o ano de nascimento da pessoa:'))
registro['idade'] = date.today().year - nascimento
registro['CTPS'] = int(input(f'Informe o número da carteira de trabalho da pessoaa [0 se não tiver]:'))
if registro['CTPS'] != 0:
    registro['ano de contatação'] = int(input('Informe o ano de sua contratação:'))
    registro['Salário'] = float(input('Informe o salário: R$'))
    registro['Idade que irá se aposentar'] = (registro['ano de contatação'] + 35) - nascimento
elif registro['CTPS'] == 0:
    registro['CTPS'] = 'Não tem'
print('-='*30)
for k, v in registro.items():
    if k == 'Salário':
        print(f'{k}: R$ {v:.2f}')
    else:
        print(f'{k}: {v}')
