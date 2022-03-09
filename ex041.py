from datetime import date
print('CLASSIFICAÇÃO DA CATEGORIA DOS ATLETAS')
nascimento=int(input('Informe o ano do nascimento do atleta:'))
idade= date.today().year - nascimento
if idade <= 9:
    print('com {} anos é um atleta MIRIM.'.format(idade))
elif idade <= 14:
    print('com {} anos é um atleta INFANTIL.'.format(idade))
elif idade <= 19:
    print('Com {} anos é um atleta JUNIOR.'.format(idade))
elif idade <= 25:
    print('Com {} anos é um atleta SÊNIOR'.format(idade))
elif idade > 25:
    print('Com {} anos é um atleta MASTER.'.format(idade))