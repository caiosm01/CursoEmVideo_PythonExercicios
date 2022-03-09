salario=float(input('Informe o salário do funcionário para ser calculado o aumento que ele irá receber: '))
if salario <= 1250.00:
    aumento= salario*0.15
    novo= salario+aumento
else:
    aumento=salario*0.1
    novo=salario+aumento
print('O aumento que esse funcionário irá receber é de {:.2f} R$. Logo, seu novo salário será de {:.2f} R$'.format(aumento, novo))