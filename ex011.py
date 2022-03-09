L=float(input('Informe somemte o valor da largura da parede, em métros:'))
H=float(input('Informe somente o valor da altura da parede, em métros:'))
A = L*H
print('Para uma parede de {:.1f} métros de largura e {:.1f} métros de altura, será necessário {:.1f} lítros de tinta.'.format(L, H, (A/2)))
