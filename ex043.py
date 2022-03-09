print('CALCULO DE IMC')
peso=float(input('Informe seu peso(kg):'))
altura=float(input('Informe sua altura(m):'))
imc=peso/(altura**2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}. você está abaixo do peso normal.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.1f}. você está no peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.1f}. você está com sobrepeso.'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.1f}. você está com obesidade.'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.1f}. você está com obesidade mórbida.'.format(imc))