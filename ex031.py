print('PROMOÇÃO!!!\nVIAGENS COM DISTÂNCIAS ATÉ 200 KM CUSTARÃO 50 CENTAVOS POR CADA QUILÔMETRO.\nVIAGENS COM DISTÂNCIAS SUPERIORES A 200KM CUSTARÃO 45 CENTAVOS POR QUILÔMETRO.')
D= float(input('Informe a distância da viagem em km: '))
if D <= 200:
    preço= D*0.5
    print('A viagem custará {:.2f} R$'.format(preço))
else:
    preço=D*0.45
    print('Como sua viagem ultrapassa os 200 km de viagem, o preço de sua passagem irá valer {:.2f} R$, com base na nossa promoção.'.format(preço))
print('Faça uma ótima viagem!')