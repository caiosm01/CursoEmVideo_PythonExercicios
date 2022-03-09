dias=int(input('Informe o número de dias que o carro foi alugado:'))
km=float(input('Informe quantos quilômetros o carro percorreu nesses dias:'))
preço=(dias*60)+(km*0.15)
print('O preço a ser pago pelo aluguel de um carro durante {} dias e que percorreu {:.2f}km é de R${:.2f}.'.format(dias, km, preço))
