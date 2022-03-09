sexo = ' '
while sexo not in 'MFMasculinoFeminino':
    sexo = str(input('Informe o sexo:')).strip().title()
    if sexo not in 'MFMasculinoFeminino' and sexo not in 'MFMasculinoFeminino':
        print('Opção inválida, tente novamente.', end=' ')
print('Sexo {} registrado com sucesso.'.format(sexo))