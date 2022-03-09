def voto(nasc):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('='*35)
nascimento = int(input('Informe o ano de nascimento:'))
print(voto(nascimento))
