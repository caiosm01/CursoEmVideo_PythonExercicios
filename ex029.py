velocidade=float(input('Informe a velocidade em km/h:'))
if velocidade > 80.0:
    multa=(velocidade-80)*7
    print('Você foi multado, pois ultrapassou a velocidade máxima que é de 80km/h. sua multa é de R${:.2f}.'.format(multa))
else:
    print('Você está dentro do limite de velocidade, que é de 80km/h.')
print('Tenha um bom dia! Dirija com atenção.')