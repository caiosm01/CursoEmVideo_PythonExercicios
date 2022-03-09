salario=float(input('Informe o salário do funcionário: R$'))
novo=salario+(salario*0.15)
print('Um funcionário que recebia R${:.2f}, com 15% de aumento passará a receber R${:.2f}.'.format(salario, novo))
