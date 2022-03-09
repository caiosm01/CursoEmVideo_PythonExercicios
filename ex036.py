valor=float(input('Informe o valor da casa:R$'))
salario=float(input('Informe o salário do comprador:R$'))
anos=int(input('Informe em quantos anos deseja pagar:'))
meses=anos*12
prestacao= valor/meses
porcento=salario*(30/100)
print('Uma casa no valor de R${:.2f} ser paga em {} anos, a prestação ficará no valor de R${:.2f} em {} vezes. '.format(valor, anos, prestacao, meses))
if prestacao <= porcento:
    print('Como o salário do comprador é de R${:.2f}, o EMPRÉSTIMO FOI APROVADO.'.format(salario))
else:
    print('Como o salário do comprador é de R${:.2f}, oEMPRÉSTIMO FOI NEGADO.'.format(salario))