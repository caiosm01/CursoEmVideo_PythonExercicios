print('{:=^40}'.format('LOJAS CAIO'))
preço=float(input('Informe o valor total da compra:R$'))
print('''Escolha sua forma de pagamento:
[1]- à vista dinheiro/cheque
[2]- à vista no cartão
[3]- em até 2x no cartão
[4]- 3x ou mais no cartão (com juros)''')
opção=int(input('Sua escolha:'))
if opção == 1:
    pagamento=preço-(preço*0.1)
    print('Com os 10% de desconto, o valor a ser pago será de R${:.2f}'.format(pagamento))
elif opção == 2:
    pagamento = preço - (preço * 0.05)
    print('Com os 5% de desconto, o valor a ser pago será de R${:.2f}'.format(pagamento))
elif opção == 3:
    parcelas=int(input('Quantas parcelas?'))
    if parcelas==1:
        print('Como não há desconto, o pagamento deve ser feito em uma parcela de R${:.2f}'.format(preço))
    elif parcelas==2:
        print('Como não há desconto, o pagamento deve ser feito em 2 parcelas de R${:.2f}'.format(preço/2))
    else:
        print('Opção inválida. Tente novamente.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas?'))
    if parcelas >= 3:
        mensalidade=(preço/parcelas)+((preço/parcelas)*0.2)
        pagamento=mensalidade*parcelas
        print('Com 20% de juros, o pagamento deve ser feito em {} parcelas de R${:.2f}. O valor total é de R${:.2f}'.format(parcelas, mensalidade,pagamento))
else:
    print('Opção inválida. Tente novamente.')